#!/usr/bin/env bash

# Use Python 3.10 on Render (works with scikit-learn 1.2.2)
echo "3.10.12" > .python-version

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
