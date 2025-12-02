# Frontend-Backend Integration Guide

## Quick Start

### 1. Start Backend
```bash
cd backend
python manage.py runserver
```
Backend will run at: `http://localhost:8000`

### 2. Start Frontend
```bash
cd ictmela-arhunt
npx serve .
```
Frontend will run at: `http://localhost:3000` (or similar)

### 3. Open in Browser
Navigate to the frontend URL and the app should automatically connect to the backend.

## Configuration

### API URL
The frontend is configured to connect to the backend at:
```javascript
API_BASE_URL: 'http://localhost:8000/api'
```

To change this (e.g., for production), edit `app.js` line 6.

### Google Form URL
Update the Google Form URL in `app.js` line 7:
```javascript
GOOGLE_FORM_URL: 'https://forms.google.com/your-form-link'
```

## How It Works

### 1. Participant Registration
- On first load, app generates a unique `device_id`
- Stored in `localStorage` for persistence
- Automatically registers with backend via `POST /api/participants/`

### 2. POI Loading
- POIs loaded from backend via `GET /api/poi/`
- No more hardcoded data
- Updates automatically if you add POIs in Django admin

### 3. Word Submission
- When user taps AR marker, prompted for secret word
- Submitted to backend via `POST /api/poi/<id>/submit/`
- Backend validates:
  - ✅ Correct word
  - ✅ Correct sequence (can't skip POIs)
  - ✅ Not already found
- Progress saved to database

### 4. Progress Tracking
- Progress loaded on app start via `GET /api/game/status/`
- Persists across page reloads
- Multiple devices can play simultaneously

### 5. Completion
- When all 6 POIs found, final modal appears
- Clicking submit checks `GET /api/game/final/`
- Opens Google Form if unlocked

## Testing the Integration

### Test Flow
1. Open frontend in browser
2. Click "Start Hunt"
3. Allow camera and location permissions
4. Find an AR marker (or simulate by clicking)
5. Enter secret word when prompted
6. Check that:
   - ✅ Correct word → Success message
   - ✅ Wrong word → Error message
   - ✅ Out of sequence → Blocked
   - ✅ Progress saved (reload page to verify)

### Backend Admin
Access Django admin at `http://localhost:8000/admin/`
- View participants
- See progress records
- Edit POI data

## API Endpoints Used

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/participants/` | POST | Register participant |
| `/api/poi/` | GET | Load POI list |
| `/api/poi/<id>/submit/` | POST | Submit secret word |
| `/api/game/status/` | GET | Get progress |
| `/api/game/final/` | GET | Check completion |

## Troubleshooting

### "Could not connect to server"
- Ensure backend is running: `python manage.py runserver`
- Check console for CORS errors
- Verify API_BASE_URL in app.js

### POIs not loading
- Check backend has POIs: `python manage.py seed_pois`
- Check browser console for errors
- Verify `/api/poi/` returns data

### Word submission fails
- Check participant is registered (check localStorage for device_id)
- Verify backend is receiving requests (check Django console)
- Check for sequence errors (must complete POIs in order)

## Production Deployment

### Backend
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Update `CORS_ALLOWED_ORIGINS` to frontend domain
4. Use PostgreSQL instead of SQLite
5. Deploy to Heroku/Railway/etc.

### Frontend
1. Update `API_BASE_URL` to production backend URL
2. Build for production (if using framework)
3. Deploy to Netlify/Vercel/etc.
