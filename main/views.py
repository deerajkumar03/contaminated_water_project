from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.timezone import now
from datetime import timedelta
from pathlib import Path
import joblib
import os

from .models import PredictionHistory


# ================= MODEL LOADING =================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "waterproj" / "ml_models" / "random_forest_model.joblib"

def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except:
        return None


# ================= HOME PAGE =================
def home_view(request):
    return render(request, "main/home.html")


# ================= LOGIN =================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("main:predict")

        messages.error(request, "Invalid username or password")

    return render(request, "main/login.html")


# ================= LOGOUT =================
@login_required(login_url="main:login")
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("main:home")


# ================= REGISTER =================
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if not username or not password1 or not password2:
            messages.error(request, "All fields required.")
            return redirect("main:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("main:register")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("main:register")

        User.objects.create_user(username=username, password=password1)
        messages.success(request, "Registration successful. Please login.")
        return redirect("main:home")

    return render(request, "main/register.html")


# ================= PREDICT VIEW (Result shown on same page) =================
@login_required(login_url="main:login")
def predict_view(request):
    ph = None
    tds = None
    prediction_result = None
    advice = None
    error_msg = None

    model = load_model()
    if model is None:
        return render(request, "main/predict.html", {
            "error": "Model not found. Train model first."
        })

    if request.method == "POST":
        ph = request.POST.get("ph_value")
        tds = request.POST.get("tds_value")

        try:
            ph = float(ph)
            tds = float(tds)
        except:
            return render(request, "main/predict.html", {
                "error": "Enter valid numeric values.",
            })

        # Model prediction
        prediction = int(model.predict([[ph, tds]])[0])

        label_map = {
            0: "Safe",
            1: "Moderate",
            2: "Contaminated"
        }

        prediction_result = label_map.get(prediction, "Unknown")

        # Advice
        if prediction_result == "Safe":
            advice = "Water is safe for drinking."
        elif prediction_result == "Moderate":
            advice = "Filtration recommended before drinking."
        else:
            advice = "Danger! Water is contaminated."

        # Save to history
        PredictionHistory.objects.create(
            user=request.user,
            ph_input=ph,
            tds_input=tds,
            result=prediction_result
        )

    return render(request, "main/predict.html", {
        "ph_value": ph,
        "tds_value": tds,
        "prediction_result": prediction_result,
        "advice": advice,
        "error": error_msg
    })


# ================= HISTORY =================
@login_required(login_url="main:login")
def history_view(request):
    history = PredictionHistory.objects.filter(
        user=request.user
    ).order_by("-prediction_date")

    return render(request, "main/history.html", {"history": history})


# ================= ADMIN VERIFY =================
def admin_verify(request):
    SUPER_KEY = "Deeraj_79899"

    if request.method == "POST":
        key = request.POST.get("super_key")

        if key == SUPER_KEY:
            request.session["admin_verified"] = True
            return redirect("main:admin_dashboard")

        messages.error(request, "Invalid Super Key")

    return render(request, "main/admin_verify.html")


# ================= ADMIN DASHBOARD =================
@login_required(login_url="main:login")
def admin_dashboard(request):
    if not request.session.get("admin_verified"):
        return redirect("main:admin_verify")

    total_users = User.objects.count()
    total_predictions = PredictionHistory.objects.count()
    active_users = User.objects.filter(
        date_joined__gte=now() - timedelta(days=30)
    ).count()
    recent_predictions = PredictionHistory.objects.filter(
        prediction_date__gte=now() - timedelta(hours=24)
    ).count()

    users_list = User.objects.all().order_by("-date_joined")
    predictions_list = PredictionHistory.objects.all().order_by("-prediction_date")

    return render(request, "main/admin_dashboard.html", {
        "total_users": total_users,
        "total_predictions": total_predictions,
        "active_users": active_users,
        "recent_predictions": recent_predictions,
        "users": users_list,
        "predictions": predictions_list,
    })
