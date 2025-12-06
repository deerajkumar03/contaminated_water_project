import os
import traceback
import re

from pathlib import Path
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

import joblib
import numpy as np

from .models import PredictionHistory

# -------------------------
# Model loader (lazy)
# -------------------------
_MODEL = None


def get_model():
    global _MODEL
    if _MODEL is None:
        # priority: settings.ML_MODEL_PATH -> waterproj/ml_models -> ml_models/
        model_path = getattr(settings, "ML_MODEL_PATH", None)
        if not model_path:
            base = getattr(settings, "BASE_DIR", None)
            if not base:
                base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            candidate = os.path.join(base, "waterproj", "ml_models", "random_forest_model.joblib")
            fallback = os.path.join(base, "ml_models", "random_forest_model.joblib")
            model_path = candidate if os.path.exists(candidate) else (fallback if os.path.exists(fallback) else candidate)

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"ML model file not found at: {model_path}")

        _MODEL = joblib.load(model_path)
    return _MODEL


# -------------------------
# Helper analytics functions
# -------------------------
def calculate_quality_index(pH, TDS):
    """Simple WQI style score (0-100)."""
    # pH score (ideal ~7.5)
    if 6.5 <= pH <= 8.5:
        ph_score = 100
    else:
        deviation = abs(pH - 7.5)
        ph_score = max(0, 100 - deviation * 20)

    # TDS score
    if TDS <= 300:
        tds_score = 100
    elif TDS <= 600:
        tds_score = 80
    elif TDS <= 900:
        tds_score = 60
    elif TDS <= 1200:
        tds_score = 40
    else:
        tds_score = 20

    return int((ph_score * 0.5) + (tds_score * 0.5))


def calculate_parameter_contribution(pH, TDS):
    """Return contribution percentages for pH and TDS (heuristic)."""
    ph_deviation = abs(pH - 7.5)
    ph_weight = ph_deviation * 10
    if TDS <= 300:
        tds_weight = 1
    elif TDS <= 600:
        tds_weight = 2
    elif TDS <= 900:
        tds_weight = 3
    elif TDS <= 1200:
        tds_weight = 4
    else:
        tds_weight = 5

    total = ph_weight + (tds_weight * 10)
    if total == 0:
        return {"pH": 50, "TDS": 50}
    return {"pH": round((ph_weight / total) * 100), "TDS": round(((tds_weight * 10) / total) * 100)}


def check_compliance(pH, TDS):
    return {
        "ph_status": "Compliant" if 6.5 <= pH <= 8.5 else "Not Compliant",
        "tds_status": "Compliant" if TDS <= 500 else "Not Compliant",
        "who_limit_ph": "6.5–8.5",
        "who_limit_tds": "<= 500 mg/L",
    }


def get_health_risk_profile(pH, TDS):
    profile = []
    if pH < 6.5:
        profile.append("Acidic water may cause stomach irritation & corrosion.")
    elif pH > 8.5:
        profile.append("Alkaline water may cause skin dryness & mineral imbalance.")
    if TDS > 900:
        profile.append("High TDS can cause kidney stress & unpleasant taste.")
    if len(profile) == 0:
        profile.append("No major health risks detected.")
    return profile


def get_action_cards(result, pH, TDS):
    cards = []
    if result == "Safe":
        cards.append("Water is safe. No action required.")
    elif result == "Moderate":
        cards.append("Consider filtration (RO/UF) before drinking.")
    else:
        cards.append("Avoid drinking immediately. Use RO and chemical disinfection.")

    if pH < 6.5:
        cards.append("Add alkaline minerals or buffering agents to balance pH.")
    elif pH > 8.5:
        cards.append("Use carbon filters to reduce alkalinity.")

    if TDS > 900:
        cards.append("Install RO purifier to remove excess dissolved solids.")

    return cards


def get_confidence(model, pH, TDS):
    try:
        proba = model.predict_proba([[pH, TDS]])[0]
        return round(np.max(proba) * 100, 2)
    except Exception:
        return "N/A"


# -------------------------
# Views: auth + pages
# -------------------------
def home(request):
    return render(request, "main/home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("main:predict")
        messages.error(request, "Invalid username or password.")
        return redirect("main:login")
    return render(request, "main/login.html")


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "Logged out.")
    return redirect("main:home")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if not username or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect("main:register")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("main:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("main:register")

        # Optional: enforce strong password server-side
        if len(password1) < 8 or not re.search(r"[A-Z]", password1) or not re.search(r"[a-z]", password1) or not re.search(r"\d", password1) or not re.search(r"[@#$%^&*!]", password1):
            messages.error(request, "Password must be 8+ chars, include upper, lower, number and special char.")
            return redirect("main:register")

        User.objects.create_user(username=username, password=password1)
        messages.success(request, "Registration successful. Please log in.")
        return redirect("main:login")
    return render(request, "main/register.html")


# -------------------------
# Forgot / Reset password
# -------------------------
def forgot_password_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        if not username:
            messages.error(request, "Enter a valid username.")
            return redirect("main:forgot_password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect("main:forgot_password")
        # For simplicity we redirect to reset page (no email flow)
        return redirect("main:reset_password", username=user.username)
    return render(request, "main/forgot_password.html")


def reset_password_view(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.error(request, "Invalid reset request.")
        return redirect("main:login")

    if request.method == "POST":
        new_password = request.POST.get("password1", "")
        confirm_password = request.POST.get("password2", "")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("main:reset_password", username=username)

        # Basic strength checks
        if len(new_password) < 8 or not re.search(r"[A-Z]", new_password) or not re.search(r"[a-z]", new_password) or not re.search(r"\d", new_password) or not re.search(r"[@#$%^&*!]", new_password):
            messages.error(request, "Password must be 8+ chars, include upper, lower, number and special character.")
            return redirect("main:reset_password", username=username)

        user.password = make_password(new_password)
        user.save()
        messages.success(request, "Password updated successfully. Please login.")
        return redirect("main:login")

    return render(request, "main/reset_password.html", {"username": username})


# -------------------------
# Prediction & History
# -------------------------
def predict_view(request):
    # If GET, render the form
    if request.method == "GET":
        return render(request, "main/predict.html")

    # POST -> perform prediction
    try:
        # accept both naming conventions from different templates
        ph_raw = request.POST.get("ph", "") or request.POST.get("ph_value", "")
        tds_raw = request.POST.get("tds", "") or request.POST.get("tds_value", "")

        ph_raw = str(ph_raw).strip()
        tds_raw = str(tds_raw).strip()

        if ph_raw == "" or tds_raw == "":
            messages.error(request, "Please provide both pH and TDS.")
            return redirect("main:predict")

        try:
            ph = float(ph_raw)
            tds = float(tds_raw)
        except ValueError:
            messages.error(request, "pH and TDS must be numeric.")
            return redirect("main:predict")

        model = get_model()
        pred = model.predict([[ph, tds]])[0]
        labels = getattr(settings, "LABEL_MAP", {0: "Safe", 1: "Moderate", 2: "Contaminated"})
        result_label = labels.get(int(pred), str(pred))

        probs = None
        confidence = "N/A"
        if hasattr(model, "predict_proba"):
            try:
                probs = model.predict_proba([[ph, tds]])[0].tolist()
                confidence = round(max(probs) * 100, 2)
            except Exception:
                probs = None

        # analytics
        wqi = calculate_quality_index(ph, tds)
        contribution = calculate_parameter_contribution(ph, tds)
        compliance = check_compliance(ph, tds)
        health_risks = get_health_risk_profile(ph, tds)
        actions = get_action_cards(result_label, ph, tds)
        confidence = get_confidence(model, ph, tds) if confidence == "N/A" else confidence

        # Save history (fields must match models.PredictionHistory)
        try:
            if request.user.is_authenticated:
                PredictionHistory.objects.create(
                    user=request.user,
                    ph_input=ph,
                    tds_input=tds,
                    result=result_label
                )
        except Exception as e:
            # Do not break prediction if history save fails
            print("Warning: failed to save history:", e)
            traceback.print_exc()

        # Render template with keys expected by predict.html
        return render(request, "main/predict.html", {
            "ph_value": ph,
            "tds_value": tds,
            "prediction_result": result_label,
            "probabilities": probs,
            "quality_index": wqi,
            "contribution": contribution,
            "compliance": compliance,
            "health_risks": health_risks,
            "actions": actions,
            "confidence": confidence,
        })

    except FileNotFoundError as e:
        traceback.print_exc()
        messages.error(request, "Model file missing on server. Contact admin.")
        return redirect("main:predict")
    except Exception as e:
        traceback.print_exc()
        messages.error(request, "Internal server error during prediction.")
        return redirect("main:predict")


@login_required(login_url="main:login")
def history_view(request):
    history = PredictionHistory.objects.filter(
        user=request.user
    ).order_by("-prediction_date")

    return render(request, "main/history.html", {"history": history})
