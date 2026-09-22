# 🚀 Deployment Guide - Water Quality Prediction System

## ✅ GitHub Repository
**Repository**: https://github.com/deerajkumar03/contaminated_water_project.git
**Status**: ✅ **UPDATED AND PUSHED**

---

## 📦 Latest Deployment (September 22, 2026)

### Latest Commits:
```
0cdcb68 - Update gitignore to exclude unused scheduler-backend folder
1b23ecc - Add comprehensive code analysis report - All systems verified and working
6fb5f56 - Improve README with proper structure and setup instructions
9f0300f - Updated model and requirements
```

---

## 🌐 Deploy to Render (Web Service)

### Step 1: Create New Web Service
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account (if not already connected)
4. Select repository: **`contaminated_water_project`**

### Step 2: Configure Service Settings
```
Name: water-quality-prediction (or any name you prefer)
Region: Choose closest to your location
Branch: main
Root Directory: (leave blank)
Runtime: Python 3
Build Command: bash build.sh
Start Command: gunicorn waterproj.wsgi:application
```

### Step 3: Environment Variables
Add these in Render dashboard under "Environment":

```bash
SECRET_KEY=your-super-secret-key-here-change-this-in-production
DEBUG=False
RENDER=True
PYTHON_VERSION=3.11.9
```

**Generate SECRET_KEY** (run in Python):
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Step 4: Set Instance Type
- **Free Tier**: Select "Free" (sleeps after inactivity)
- **Starter**: $7/month (always on, faster)

### Step 5: Deploy!
Click **"Create Web Service"** and wait 3-5 minutes for deployment.

---

## 🔧 Post-Deployment Steps

### 1. Update ALLOWED_HOSTS
Once Render gives you the URL (e.g., `your-app.onrender.com`), update:

**File**: `waterproj/settings.py`
```python
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "your-app.onrender.com",  # Add your new Render URL
]

CSRF_TRUSTED_ORIGINS = [
    "https://your-app.onrender.com",  # Add your new Render URL
]
```

### 2. Push Changes
```bash
git add waterproj/settings.py
git commit -m "Update ALLOWED_HOSTS for new Render deployment"
git push origin main
```

Render will automatically redeploy.

### 3. Create Superuser (Optional)
Open Render Shell from dashboard and run:
```bash
python manage.py createsuperuser
```

---

## 🌍 Deploy to Other Platforms

### Heroku
```bash
# Install Heroku CLI
heroku login
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

### Railway
1. Go to [Railway.app](https://railway.app/)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select `contaminated_water_project`
4. Railway auto-detects settings
5. Add environment variables in Variables tab

### PythonAnywhere
1. Upload code via Git
2. Set up virtual environment
3. Configure WSGI file
4. Add static files mapping

---

## 📋 Deployment Checklist

Before deploying, ensure:

- [x] `requirements.txt` has all dependencies
- [x] `Procfile` exists with correct command
- [x] `runtime.txt` specifies Python version
- [x] `build.sh` script is executable
- [x] `.gitignore` excludes sensitive files
- [x] `SECRET_KEY` is in environment variables
- [x] `DEBUG=False` in production
- [x] `ALLOWED_HOSTS` includes your domain
- [x] `CSRF_TRUSTED_ORIGINS` includes your domain
- [x] Static files collected with WhiteNoise
- [x] ML model file exists in `waterproj/ml_models/`

---

## 🐛 Troubleshooting

### Issue: "Application Error" on Render
**Solution**: Check Render logs for specific error
```bash
# In Render dashboard, go to Logs tab
```

### Issue: Static files not loading
**Solution**: Run collectstatic
```bash
python manage.py collectstatic --noinput
```

### Issue: Database errors
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Issue: ModuleNotFoundError
**Solution**: Update requirements.txt and redeploy
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

### Issue: Cold start delays (Free tier)
**Expected**: Free tier sleeps after 15 min inactivity
**Solution**: Upgrade to Starter tier or use keep-alive service

---

## 📊 Monitoring

### Check Application Health
- **Render**: Dashboard → Logs
- **GitHub**: Actions tab (if using CI/CD)

### Performance Metrics
- Response time: ~200-500ms (first load may be slower)
- Cold start: ~30s on free tier
- Model prediction: <100ms

---

## 🔐 Security Best Practices

1. ✅ Never commit `.env` files
2. ✅ Use environment variables for secrets
3. ✅ Set `DEBUG=False` in production
4. ✅ Keep `SECRET_KEY` secure
5. ✅ Use HTTPS only (enforced by Render)
6. ✅ Regular dependency updates
7. ✅ Monitor logs for suspicious activity

---

## 📞 Support

**Repository**: https://github.com/deerajkumar03/contaminated_water_project
**Author**: Deeraj Kumar
**Issues**: Open GitHub issue for bugs

---

## ✅ Current Status

**Repository**: ✅ Up to date
**Code Quality**: ✅ All tests passing
**Documentation**: ✅ Complete
**Ready to Deploy**: ✅ YES

### Active Deployments:
1. **Render**: https://contaminated-water-project-u533.onrender.com/ (LIVE)

---

*Last Updated: September 22, 2026*
*Deployment Guide v1.0*
