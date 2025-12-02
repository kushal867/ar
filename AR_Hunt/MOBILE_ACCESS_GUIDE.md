# 📱 AR Hunt - Mobile Access Guide

## ✅ Your App is Ready for Mobile!

### 🌐 Access URLs

**From your mobile device (connected to same WiFi):**
- **Frontend**: `http://192.168.0.104:3000`
- **Backend API**: `http://192.168.0.104:8000/api`

**From your computer:**
- **Frontend**: `http://localhost:3000`
- **Backend API**: `http://localhost:8000/api`

---

## 🚀 Quick Start

### 1. Servers are Running ✅

**Backend** (Django):
```bash
python manage.py runserver 0.0.0.0:8000
```
✅ Now accepting connections from network devices

**Frontend** (Static Server):
```bash
npm start
```
✅ Serving on `http://192.168.0.104:3000`

### 2. Connect from Mobile

1. **Ensure same WiFi**: Your phone and computer must be on the same WiFi network
2. **Open browser**: Use Chrome (Android) or Safari (iPhone)
3. **Navigate to**: `http://192.168.0.104:3000`
4. **Allow permissions**: 
   - Camera (for AR and QR scanning)
   - Location (or use Dev Mode)

---

## 🔧 Configuration Details

### Frontend Auto-Detection

The app automatically detects where it's being accessed from:

```javascript
// From app.js (lines 5-9)
API_BASE_URL: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:8000/api'      // Desktop
    : 'http://192.168.0.104:8000/api'  // Mobile
```

**This means:**
- ✅ Desktop users automatically use `localhost:8000`
- ✅ Mobile users automatically use `192.168.0.104:8000`
- ✅ No manual configuration needed!

### Backend Network Binding

**Important**: Backend must run with `0.0.0.0:8000` to accept network connections:

```bash
# ❌ Wrong - only accepts localhost
python manage.py runserver

# ✅ Correct - accepts network connections
python manage.py runserver 0.0.0.0:8000
```

### Django Settings

Already configured in `settings.py`:
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.104', '192.168.0.101', '*']
CORS_ALLOW_ALL_ORIGINS = True  # For development
```

---

## 📱 Mobile Testing Checklist

### Before Testing
- [ ] Backend running with `0.0.0.0:8000`
- [ ] Frontend running (npm start)
- [ ] Phone on same WiFi as computer
- [ ] Firewall allows port 8000 (Windows)

### On Mobile Device
- [ ] Open `http://192.168.0.104:3000`
- [ ] See "Start Hunt" button
- [ ] Click "Start Hunt"
- [ ] Allow camera permission
- [ ] See AR view with camera feed
- [ ] See "DEV MODE" badge (orange, top-right)
- [ ] GPS status shows green (dev mode)
- [ ] Bottom panel shows POIs list

### Test Features
- [ ] Tap AR marker (if visible)
- [ ] Enter secret word (e.g., "Kickstart")
- [ ] See success message
- [ ] Progress updates in POIs tab
- [ ] QR scanner toggle works
- [ ] Backend connection confirmed

---

## 🐛 Troubleshooting

### Issue: "Cannot connect to server"

**Solution 1: Check WiFi**
- Ensure phone and computer on same network
- Check WiFi name on both devices

**Solution 2: Check Firewall**
```bash
# Windows: Allow Python through firewall
1. Windows Security → Firewall & network protection
2. Allow an app through firewall
3. Find Python → Check "Private networks"
```

**Solution 3: Verify Backend**
```bash
# Should see this in terminal:
Starting development server at http://0.0.0.0:8000/
```

**Solution 4: Test Backend Manually**
Open on mobile browser: `http://192.168.0.104:8000/api/poi/`
- Should see JSON list of POIs
- If this works, backend is accessible!

### Issue: "QR Scanning Disabled"

This means backend is not reachable. Check:
1. Backend running with `0.0.0.0:8000`
2. Firewall allows connections
3. Same WiFi network
4. Try accessing `http://192.168.0.104:8000/api/poi/` directly

### Issue: Camera not working

**iPhone Safari:**
```
Settings → Safari → Camera → Allow
```

**Android Chrome:**
```
Settings → Apps → Chrome → Permissions → Camera → Allow
```

Then refresh the page.

### Issue: GPS not working

**For Testing**: Dev Mode is enabled by default!
- Uses mock GPS coordinates
- No permission needed
- See orange "DEV MODE" badge

**For Production**: Requires HTTPS
- Deploy to secure server
- Set `DEV_MODE: false` in app.js

---

## 🔍 Verification Commands

### Check Your Computer's IP
```bash
# Windows
ipconfig

# Look for "IPv4 Address" under WiFi adapter
# Should be: 192.168.0.104
```

### Test Backend from Computer
```bash
# Should return JSON
curl http://localhost:8000/api/poi/
curl http://192.168.0.104:8000/api/poi/
```

### Check Running Servers
```bash
# Backend should show:
Starting development server at http://0.0.0.0:8000/

# Frontend should show:
- Local:    http://localhost:3000
- Network:  http://192.168.0.104:3000
```

---

## 📊 Network Flow

```
Mobile Device (192.168.0.101)
    ↓
    ↓ Access: http://192.168.0.104:3000
    ↓
Computer (192.168.0.104)
    ├─→ Frontend Server (port 3000)
    │   └─→ Serves: index.html, app.js, style.css
    │
    └─→ Backend Server (port 8000)
        └─→ API: /api/poi/, /api/participants/, etc.
```

---

## 🎯 Expected Behavior

### On Desktop (`localhost:3000`)
1. App loads
2. Connects to `http://localhost:8000/api`
3. Registers participant
4. Loads POIs
5. Shows AR view

### On Mobile (`192.168.0.104:3000`)
1. App loads
2. Auto-detects network access
3. Connects to `http://192.168.0.104:8000/api`
4. Registers participant
5. Loads POIs
6. Shows AR view with camera
7. QR scanning enabled (if backend connected)

---

## 💡 Tips

1. **Keep terminal windows open** to see API requests in real-time
2. **Use Chrome DevTools** on mobile for debugging (chrome://inspect)
3. **Check browser console** for error messages
4. **Test backend first** before testing frontend
5. **Restart servers** if you change configuration

---

## 🔐 Security Note

> [!WARNING]
> Current settings (`CORS_ALLOW_ALL_ORIGINS = True`, `ALLOWED_HOSTS = ['*']`) are for **development only**. 
> 
> For production deployment:
> - Use specific ALLOWED_HOSTS
> - Configure CORS properly
> - Use HTTPS
> - Set DEBUG = False

---

## ✅ Success Indicators

You'll know it's working when:
- ✅ Mobile browser loads the app
- ✅ Camera feed shows in AR view
- ✅ Orange "DEV MODE" badge visible
- ✅ GPS status is green
- ✅ POIs list shows 6 locations
- ✅ Backend connection confirmed
- ✅ QR scanner toggle is enabled
- ✅ No error messages in console

**Happy Hunting! 🎯**
