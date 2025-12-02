# Render Deployment Guide for AR Hunt Backend

## Problem Fixed
The `ModuleNotFoundError: No module named 'ar_hunt_backend'` error occurred because the Django project is located in `AR_Hunt/backend/` but Render was trying to run gunicorn from the repository root.

## Solution Overview
Created deployment configuration files that ensure gunicorn runs from the correct directory.

## Files Created

### 1. `render.yaml` (Root of repository)
Configures the Render service with proper build and start commands.

### 2. `build.sh` (Root of repository)
Build script that:
- Navigates to the Django project directory
- Installs dependencies
- Collects static files
- Runs migrations

### 3. `start.sh` (Root of repository)
Start script that:
- Navigates to the Django project directory
- Runs gunicorn with the correct module path

## Configuration in Render Dashboard

If you prefer to configure via the Render dashboard instead of using `render.yaml`:

1. **Build Command:**
   ```bash
   cd AR_Hunt/backend && pip install -r ../../requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
   ```

2. **Start Command:**
   ```bash
   cd AR_Hunt/backend && gunicorn ar_hunt_backend.wsgi:application --bind 0.0.0.0:$PORT
   ```

3. **Environment Variables to Set:**
   - `PYTHON_VERSION`: `3.13.4`
   - `SECRET_KEY`: (Generate a new secret key for production)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Render domain (e.g., `your-app.onrender.com`)

## Next Steps

1. **Commit and push all changes to your repository:**
   ```bash
   git add .
   git commit -m "Fix Render deployment configuration"
   git push
   ```

2. **In Render Dashboard:**
   - If using `render.yaml`: Render will automatically detect and use it
   - If configuring manually: Update the Build Command and Start Command as shown above

3. **Set Environment Variables:**
   - Go to your service settings in Render
   - Add the environment variables listed above
   - Generate a secure SECRET_KEY (you can use Django's `get_random_secret_key()`)

4. **Deploy:**
   - Trigger a manual deploy or wait for auto-deploy
   - Monitor the logs to ensure successful deployment

## Updated Dependencies
- Added `whitenoise` for serving static files in production
- Updated Django settings to use environment variables for security

## Security Improvements
- SECRET_KEY now uses environment variable
- DEBUG mode controlled via environment variable (defaults to False)
- WhiteNoise configured for efficient static file serving
- Static files properly configured with STATIC_ROOT
