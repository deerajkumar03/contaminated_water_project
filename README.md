# 💧 Contaminated Water Prediction System

A full-stack Machine Learning web application built using Django that predicts water quality (Safe / Moderate / Contaminated) based on multiple chemical parameters.

The system uses a trained Random Forest model to analyze water characteristics and determine whether the water is safe for consumption.

---

## 🚀 Features

- User Registration and Login system
- Water quality prediction using Machine Learning
- Stores prediction history for each user
- Admin-only dashboard with verification
- Random Forest model loaded using `.joblib`
- Input validation for user data
- Simple and clean user interface

---

## 🧠 Machine Learning Model

- Algorithm: Random Forest Classifier
- Training Script: `model_training.py`
- Saved Model: `waterproj/ml_models/random_forest_model.joblib`

### Input Features

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

### Output Classes

- 0 → Safe
- 1 → Moderate
- 2 → Contaminated

---

## 🗂 Project Structure
contaminated_water_project/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── waterproj/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── ml_models/
│ └── random_forest_model.joblib
│
└── main/
├── views.py
├── models.py
├── urls.py
├── templates/
└── static/


---

## ⚙️ Setup Instructions (Local Machine)

### 1. Clone the Repository

```bash
git clone https://github.com/deerajkumar03/contaminated_water_project.git
cd contaminated_water_project

##2. Create Virtual Environment
python -m venv env

//Activate the environment://
Windows:

env\Scripts\activate

Mac/Linux:

source env/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Server
python manage.py runserver

6. Open in Browser
http://127.0.0.1:8000/

📚 Tech Stack

Backend: Django (Python)

Machine Learning: Scikit-learn (Random Forest)

Frontend: HTML, CSS, JavaScript

Database: SQLite (for development)

📌 Future Improvements

Deploy the application on cloud (Render / AWS)

Add REST API for predictions

Improve UI/UX

Add visualization dashboards

👨‍💻 Author

Deeraj Kumar
MCA Student | Full Stack Developer | Machine Learning Enthusiast
