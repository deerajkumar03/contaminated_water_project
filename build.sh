#!/usr/bin/env bash

# Force Render to use Python 3.12.1
echo "3.12.1" > .python-version

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
