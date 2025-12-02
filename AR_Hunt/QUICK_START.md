# AR Hunt - Quick Start Guide

## Starting the Servers

### Backend (Django)
```bash
cd backend
python manage.py runserver 0.0.0.0:8000
```

**Or use the startup script:**
- Windows: Double-click `backend/start_backend.bat`
- Mac/Linux: Run `bash backend/start_backend.sh`

The backend will be accessible from:
- `http://localhost:8000` (local)
- `http://192.168.0.104:8000` (network)
- `http://<any-ip>:8000` (any device on your network)

### Frontend (Web App)
```bash
cd ictmela-arhunt
npm start
```

The frontend will be accessible from:
- `http://localhost:3000` (local)
- `http://192.168.0.104:3000` (network)

## Testing from Mobile

1. **Connect to same WiFi** as your computer
2. **Open browser** on mobile device
3. **Navigate to** `http://192.168.0.104:3000`
4. **Check console** for any errors (use remote debugging if needed)

## Troubleshooting

### "Could not load POIs from server"

**Check:**
1. ✅ Backend is running on `0.0.0.0:8000`
2. ✅ Frontend can access `http://<your-ip>:8000/api/poi/`
3. ✅ Both devices on same WiFi network
4. ✅ Firewall allows port 8000

**Test backend manually:**
```bash
curl http://192.168.0.104:8000/api/poi/
```

Should return JSON with 6 POIs.

### Check Current IP Address

**Windows:**
```bash
ipconfig
```
Look for "IPv4 Address" under your WiFi adapter

**Mac/Linux:**
```bash
ifconfig
```
Look for "inet" address

## API Endpoints

- `GET /api/poi/` - List all POIs
- `GET /api/poi/{id}/` - Get single POI
- `POST /api/participants/` - Register participant
- `POST /api/poi/{id}/submit/` - Submit secret word
- `GET /api/game/status/?device_id=<id>` - Get game status
- `GET /api/game/final/?device_id=<id>` - Check final unlock
