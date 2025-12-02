# URGENT: Render Dashboard Configuration Fix

## The Problem
Render is **NOT** using the `render.yaml` file. It's using old manual configuration from the dashboard, which is why you're still getting the `ModuleNotFoundError`.

## The Solution - Update Render Dashboard Settings

You **MUST** go to your Render dashboard and manually update these settings:

### Step 1: Go to Your Service Settings
1. Log in to [Render Dashboard](https://dashboard.render.com/)
2. Click on your `ar-hunt-backend` service
3. Click on **"Settings"** in the left sidebar

### Step 2: Update Build Command
Scroll to **"Build Command"** and replace it with:
```bash
cd AR_Hunt/backend && pip install -r ../../requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
```

### Step 3: Update Start Command
Scroll to **"Start Command"** and replace it with:
```bash
cd AR_Hunt/backend && gunicorn ar_hunt_backend.wsgi:application --bind 0.0.0.0:$PORT
```

### Step 4: Save Changes
Click **"Save Changes"** at the bottom of the page.

### Step 5: Manual Deploy
After saving, click **"Manual Deploy"** → **"Deploy latest commit"**

---

## Alternative: Use render.yaml (Recommended)

If you want Render to use the `render.yaml` file instead:

### Option A: Delete the Service and Recreate
1. Delete the current service from Render dashboard
2. Create a new Web Service
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml` and use it

### Option B: Clear Manual Configuration
1. In service settings, look for an option to "Use render.yaml"
2. Or delete all manual build/start commands to let Render auto-detect the yaml file

---

## Environment Variables (Important!)

While you're in the settings, add these environment variables:

| Variable | Value | Why |
|----------|-------|-----|
| `SECRET_KEY` | `<generate-new-key>` | Django security |
| `DEBUG` | `False` | Disable debug in production |
| `ALLOWED_HOSTS` | `your-app.onrender.com` | Allow your domain |

**Generate a new SECRET_KEY** using this Python command:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## Quick Test Locally

To verify the commands work, test locally:

```bash
cd c:/Users/kusha/OneDrive/Desktop/jkj/logics
cd AR_Hunt/backend
pip install -r ../../requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
gunicorn ar_hunt_backend.wsgi:application --bind 0.0.0.0:8000
```

If this works locally, it will work on Render with the correct configuration.

---

## Why This Happened

Render prioritizes **manual dashboard configuration** over `render.yaml`. Since you had manual settings configured before we added the yaml file, Render is still using those old settings.

## Next Steps

1. ✅ Update Build Command in Render dashboard
2. ✅ Update Start Command in Render dashboard  
3. ✅ Save changes
4. ✅ Trigger manual deploy
5. ✅ Monitor deployment logs
6. ✅ Add environment variables (optional but recommended)
