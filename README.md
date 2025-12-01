📌 Contaminated Water Prediction System

A Machine Learning + Django web application that predicts the quality of water (Safe / Moderate / Contaminated) using PH and TDS values. The prediction engine is powered by a Random Forest Classifier trained on real-world water quality data.

🚀 Features

User Registration & Login

Water Quality Prediction using ML

Stores Prediction History for Each User

Admin-Only Dashboard

Random Forest model stored as .joblib for optimized loading

Clean UI for PH & TDS input

Error handling for invalid inputs

Secure admin verification

🧠 Machine Learning Model

Algorithm: Random Forest Classifier

Training File: model_training.py

Final deployed model:

waterproj/ml_models/random_forest_model.joblib


Input Features:

PH value

TDS value

Output Classes:

0 → Safe

1 → Moderate

2 → Contaminated

🗂 Project Folder Structure
contaminated_water_project/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── waterproj/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ml_models/
│       └── random_forest_model.joblib
│
└── main/
    ├── views.py
    ├── models.py
    ├── urls.py
    ├── templates/
    └── static/

⚙️ Setup Instructions (Local Machine)
1. Clone the Repository
git clone <repo-link>
cd contaminated_water_project

2. Create Virtual Environment
python -m venv env
source env/bin/activate      # Mac/Linux
env\Scripts\activate         # Windows

3. Install Requirements
pip install -r requirements.txt

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Run Server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

🔐 Admin Dashboard

To access the admin dashboard:

Login as normal user

Visit /admin-verify/

Enter the Super Key

Deeraj_79899

📚 Tech Stack

Backend: Django

Machine Learning: Scikit-Learn (Random Forest)

Frontend: HTML, CSS, JS

Database: SQLite (local)

Deployment: GitHub-ready (Render deployment optional)

👨‍💻 Author

Deeraj Kumar
MCA Student | Full Stack Developer | ML Enthusiast