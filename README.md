<div align="center">

# 💧 Contaminated Water Prediction System

### AI-Powered Water Quality Analysis Platform

[![Live Demo](https://img.shields.io/badge/Demo-Live-success?style=for-the-badge&logo=render)](https://contaminated-water-project-u533.onrender.com/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/deerajkumar03/contaminated_water_project)
[![Django](https://img.shields.io/badge/Django-4.2.7-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![ML](https://img.shields.io/badge/ML-Random_Forest-F7931E?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)

<p align="center">
  <img src="https://img.shields.io/badge/Status-Production_Ready-success?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Maintained-Yes-green?style=flat-square" />
</p>

**A full-stack Machine Learning web application that predicts water quality based on pH and TDS values using Random Forest algorithm. Helps ensure water safety with real-time predictions and comprehensive analytics.**

[🚀 Live Demo](https://contaminated-water-project-u533.onrender.com/) • [📖 Documentation](DEPLOYMENT_GUIDE.md) • [🐛 Report Bug](https://github.com/deerajkumar03/contaminated_water_project/issues)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🎯 Key Highlights](#-key-highlights)
- [🧠 Machine Learning Model](#-machine-learning-model)
- [🏗️ Tech Stack](#️-tech-stack)
- [📸 Screenshots](#-screenshots)
- [⚙️ Installation](#️-installation)
- [🚀 Deployment](#-deployment)
- [📁 Project Structure](#-project-structure)
- [🔐 Security Features](#-security-features)
- [🤝 Contributing](#-contributing)
- [👨‍💻 Author](#-author)

---

## ✨ Features

### 🔐 **User Management**
- ✅ Secure user registration with password strength validation
- ✅ Login/Logout functionality with session management
- ✅ Password reset and recovery system
- ✅ User-specific prediction history tracking

### 🧪 **Water Quality Prediction**
- ✅ **Real-time predictions** using trained Random Forest model
- ✅ **Input validation** for pH (0-14) and TDS (0-1500 mg/L)
- ✅ **Three-tier classification**: Safe, Moderate, Contaminated
- ✅ **Confidence score** for each prediction

### 📊 **Advanced Analytics**
- ✅ **Water Quality Index (WQI)** calculation
- ✅ **WHO/BIS Compliance** checking
- ✅ **Parameter Contribution** analysis (pH vs TDS influence)
- ✅ **Health Risk Assessment** based on water parameters
- ✅ **Treatment Recommendations** for contaminated water

### 🎨 **Modern UI/UX**
- ✅ Glass morphism design with gradient backgrounds
- ✅ Responsive layout for all devices
- ✅ Interactive forms with client-side validation
- ✅ Real-time error feedback
- ✅ Clean and intuitive navigation

### 🔧 **Admin Panel**
- ✅ Django admin interface for data management
- ✅ Prediction history monitoring
- ✅ User management capabilities

---

## 🎯 Key Highlights

<table>
  <tr>
    <td align="center">🚀<br/><b>Fast Predictions</b><br/>< 100ms response time</td>
    <td align="center">🎯<br/><b>High Accuracy</b><br/>85%+ model accuracy</td>
    <td align="center">📱<br/><b>Responsive Design</b><br/>Works on all devices</td>
    <td align="center">🔒<br/><b>Secure</b><br/>CSRF & Password protection</td>
  </tr>
  <tr>
    <td align="center">☁️<br/><b>Cloud Deployed</b><br/>Live on Render</td>
    <td align="center">📊<br/><b>Analytics</b><br/>Advanced water insights</td>
    <td align="center">💾<br/><b>History Tracking</b><br/>All predictions saved</td>
    <td align="center">🎨<br/><b>Modern UI</b><br/>Glass morphism design</td>
  </tr>
</table>

---

## 🧠 Machine Learning Model

### Algorithm: **Random Forest Classifier**

**Why Random Forest?**
- Handles non-linear relationships effectively
- Resistant to overfitting
- Provides feature importance insights
- Fast prediction time

### Model Details

```python
Algorithm: Random Forest Classifier
Estimators: 150 trees
Training Data: 1500+ samples
Features: pH, TDS
Classes: Safe (0), Moderate (1), Contaminated (2)
Accuracy: ~85%+
```

### Input Features

| Feature | Description | Valid Range |
|---------|-------------|-------------|
| **pH** | Measure of water acidity/alkalinity | 0 - 14 |
| **TDS** | Total Dissolved Solids (mg/L) | 0 - 1500 |

### Output Classes

| Class | Label | Meaning |
|-------|-------|---------|
| **0** | 🟢 Safe | Water is safe for consumption |
| **1** | 🟡 Moderate | Water needs filtration before use |
| **2** | 🔴 Contaminated | Water is unsafe - avoid consumption |

### Model Files

- **Training Script**: `model_training.py`
- **Saved Model**: `waterproj/ml_models/random_forest_model.joblib`
- **Format**: Joblib (optimized for scikit-learn)

---

## 🏗️ Tech Stack

### Backend
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2.7-092E20?logo=django)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2.2-F7931E?logo=scikit-learn&logoColor=white)

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Font Awesome](https://img.shields.io/badge/Font_Awesome-528DD7?logo=fontawesome&logoColor=white)

### Database & Storage
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![WhiteNoise](https://img.shields.io/badge/WhiteNoise-Static_Files-lightgrey)

### ML Libraries
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-1.3.2-orange)

### Deployment
![Render](https://img.shields.io/badge/Render-46E3B7?logo=render&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-21.2.0-499848?logo=gunicorn&logoColor=white)

---

## 📸 Screenshots

### 🏠 Home Page
Beautiful landing page with glass morphism design and water-themed background.

### 🔐 Authentication
Secure login and registration with password strength validation and recovery options.

### 🧪 Prediction Interface
Clean, intuitive form for entering pH and TDS values with real-time validation.

### 📊 Results Dashboard
Comprehensive analytics including WQI, compliance status, health risks, and recommendations.

### 📜 History
Track all previous predictions with date, time, and results.

---

## ⚙️ Installation

### Prerequisites

- Python 3.11+ installed
- Git installed
- Virtual environment tool (recommended)

### Local Setup

1. **Clone the Repository**
```bash
git clone https://github.com/deerajkumar03/contaminated_water_project.git
cd contaminated_water_project
```

2. **Create Virtual Environment**
```bash
# Windows
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate
```

3. **Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create Superuser (Optional)**
```bash
python manage.py createsuperuser
```

6. **Collect Static Files**
```bash
python manage.py collectstatic --noinput
```

7. **Run Development Server**
```bash
python manage.py runserver
```

8. **Open in Browser**
```
http://127.0.0.1:8000/
```

---

## 🚀 Deployment

### Deploy to Render

1. **Fork/Clone this repository**

2. **Create New Web Service on Render**
   - Connect your GitHub repository
   - Select branch: `main`

3. **Configure Build Settings**
```bash
Build Command: bash build.sh
Start Command: gunicorn waterproj.wsgi:application
```

4. **Add Environment Variables**
```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
RENDER=True
PYTHON_VERSION=3.11.9
```

5. **Deploy!**
   - Render will automatically deploy your application
   - Update `ALLOWED_HOSTS` with your Render URL

📖 **Detailed Guide**: See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 📁 Project Structure

```
contaminated_water_project/
│
├── 📄 manage.py                    # Django management script
├── 📄 requirements.txt             # Python dependencies
├── 📄 Procfile                     # Render deployment config
├── 📄 runtime.txt                  # Python version
├── 📄 build.sh                     # Build script
├── 📄 README.md                    # Project documentation
├── 📄 DEPLOYMENT_GUIDE.md          # Deployment instructions
├── 📄 ANALYSIS_REPORT.md           # Code analysis report
│
├── 📁 waterproj/                   # Django project settings
│   ├── 📄 settings.py              # Configuration
│   ├── 📄 urls.py                  # URL routing
│   ├── 📄 wsgi.py                  # WSGI config
│   └── 📁 ml_models/               # Machine Learning models
│       └── 📄 random_forest_model.joblib
│
├── 📁 main/                        # Main Django app
│   ├── 📄 views.py                 # View functions
│   ├── 📄 models.py                # Database models
│   ├── 📄 urls.py                  # App URLs
│   ├── 📄 admin.py                 # Admin configuration
│   ├── 📁 templates/               # HTML templates
│   │   └── 📁 main/
│   │       ├── 📄 home.html
│   │       ├── 📄 login.html
│   │       ├── 📄 register.html
│   │       ├── 📄 predict.html
│   │       ├── 📄 history.html
│   │       └── 📄 base.html
│   └── 📁 migrations/              # Database migrations
│
├── 📁 static/                      # Static files (CSS, JS)
├── 📁 staticfiles/                 # Collected static files
└── 📄 db.sqlite3                   # SQLite database
```

---

## 🔐 Security Features

- ✅ **CSRF Protection** enabled for all forms
- ✅ **Password Hashing** using Django's secure hashing
- ✅ **Password Strength Validation** (8+ chars, mixed case, numbers, symbols)
- ✅ **SQL Injection Protection** via Django ORM
- ✅ **XSS Protection** with template escaping
- ✅ **Session Security** with secure cookies in production
- ✅ **HTTPS Enforcement** on production deployment
- ✅ **Input Validation** for all user inputs

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. ✍️ Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔁 Open a Pull Request

### Areas for Contribution

- 🎨 UI/UX improvements
- 🧪 Additional ML models
- 📊 More analytics features
- 🌐 API development
- 📱 Mobile app integration
- 🧪 Unit tests
- 📚 Documentation improvements

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**Deeraj Kumar**

MCA Student | Full Stack Developer | ML Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-deerajkumar03-181717?style=for-the-badge&logo=github)](https://github.com/deerajkumar03)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:deerajkumar03@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/deerajkumar03)

</div>

---

## 🙏 Acknowledgments

- WHO Guidelines for water quality standards
- BIS (Bureau of Indian Standards) for compliance metrics
- Scikit-learn community for ML algorithms
- Django community for the excellent framework
- Unsplash for beautiful water-themed images

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Made with 💙 and ☕ by [Deeraj Kumar](https://github.com/deerajkumar03)**

</div>
