# Mobile Phone Setup Guide

## Quick Start for Mobile Testing

### 1. Start Backend on Computer
```bash
cd backend
python manage.py runserver 0.0.0.0:8000
```
**Important**: Use `0.0.0.0:8000` to allow network access (not just `runserver`)

### 2. Start Frontend on Computer
```bash
cd ictmela-arhunt
npm start
```
Note the Network URL: `http://192.168.0.104:3000`

### 3. Connect from Mobile Phone

**On your mobile phone:**
1. Connect to the **same WiFi network** as your computer
2. Open browser (Chrome/Safari)
3. Go to: `http://192.168.0.104:3000`
4. App should load! ✅

## How It Works

### Auto-Detection
The frontend now automatically detects where it's being accessed from:

- **Desktop** (localhost): Uses `http://localhost:8000/api`
- **Mobile** (network): Uses `http://192.168.0.104:8000/api`

### Backend Configuration
Django is configured to accept connections from:
- `localhost` (desktop)
- `127.0.0.1` (desktop)
- `192.168.0.104` (your computer's IP)
- `192.168.0.101` (mobile phone IP)
- `*` (any IP - for development only)

## Troubleshooting

### Issue: "Cannot connect to server"

**Check 1: Same WiFi Network**
- Computer and phone must be on same WiFi
- Check WiFi name on both devices

**Check 2: Firewall**
- Windows Firewall might block port 8000
- Allow Python through firewall:
  1. Windows Security → Firewall
  2. Allow an app
  3. Find Python → Allow Private networks

**Check 3: Backend Running**
- Ensure backend started with `0.0.0.0:8000`
- Check terminal shows: `Starting development server at http://0.0.0.0:8000/`

**Check 4: Correct IP Address**
- Your computer's IP might be different
- Find your IP:
  ```bash
  ipconfig
  ```
- Look for "IPv4 Address" under WiFi adapter
- Update `app.js` line 9 if different from `192.168.0.104`

### Issue: GPS Permission on Mobile

**For Testing:**
- DEV_MODE is enabled by default
- Uses mock GPS coordinates
- No permission needed!

**For Production:**
1. Deploy to HTTPS (required for GPS on mobile)
2. Set `DEV_MODE: false` in app.js
3. Allow location when prompted

## Testing the Full Flow on Mobile

1. **Open app on mobile**: `http://192.168.0.104:3000`
2. **See DEV MODE badge**: Orange badge confirms dev mode active
3. **Click "Start Hunt"**: App initializes
4. **Check console** (if using Chrome remote debugging):
   - Should see: "Participant registered"
   - Should see: "Loaded POIs from backend"
5. **Tap AR marker**: (or simulate by tapping screen)
6. **Enter secret word**: e.g., "Kickstart"
7. **Backend validates**: Check computer terminal for API calls
8. **Progress saved**: ✅

## Network URLs Reference

**Frontend:**
- Desktop: `http://localhost:3000`
- Mobile: `http://192.168.0.104:3000`

**Backend API:**
- Desktop: `http://localhost:8000/api`
- Mobile: `http://192.168.0.104:8000/api`

**Django Admin:**
- Desktop: `http://localhost:8000/admin`
- Mobile: `http://192.168.0.104:8000/admin`

## Production Deployment

For actual deployment (not local testing):

1. **Backend**: Deploy to Heroku/Railway/etc.
   - Get production URL: e.g., `https://ar-hunt-api.herokuapp.com`
   
2. **Frontend**: Update `app.js` line 9:
   ```javascript
   API_BASE_URL: 'https://ar-hunt-api.herokuapp.com/api'
   ```

3. **Deploy Frontend**: Netlify/Vercel/etc.

4. **HTTPS Required**: Mobile GPS only works with HTTPS in production
