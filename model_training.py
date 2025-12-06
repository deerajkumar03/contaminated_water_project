import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

CSV_FILE = "water_quality.csv"
MODEL_FILE = "model.pkl"

# Load dataset
if os.path.exists(CSV_FILE):
    print("Loading dataset:", CSV_FILE)
    df = pd.read_csv(CSV_FILE)
else:
    print("Dataset not found. Creating synthetic dataset...")

    N = 1500
    ph = np.round(np.random.uniform(4.5, 9.5, N), 2)
    tds = np.round(np.random.uniform(50, 2000, N), 2)

    labels = []
    for p, t in zip(ph, tds):
        if (6.5 <= p <= 8.5) and (t < 500):
            labels.append(0)
        elif (6.0 <= p <= 9.0) and (t < 1000):
            labels.append(1)
        else:
            labels.append(2)

    df = pd.DataFrame({"pH": ph, "TDS": tds, "label": labels})
    df.to_csv(CSV_FILE, index=False)
    print("Synthetic dataset saved as water_quality.csv")

# Train model using CORRECT column names
X = df[["pH", "TDS"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, MODEL_FILE)
print("model.pkl created successfully!")
