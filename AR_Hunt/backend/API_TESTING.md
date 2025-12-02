# API Testing Script for AR Campus Hunt Backend

This script demonstrates how to test the Django backend API endpoints.

## Prerequisites
```bash
# Start the Django server
cd backend
python manage.py runserver
```

## Test Endpoints

### 1. Get All POIs
```bash
curl http://localhost:8000/api/poi/
```

### 2. Get Single POI
```bash
curl http://localhost:8000/api/poi/1/
```

### 3. Get QR Code for POI
```bash
curl http://localhost:8000/api/poi/1/qr/
```

### 4. Register a Participant
```bash
curl -X POST http://localhost:8000/api/participants/ \
  -H "Content-Type: application/json" \
  -d '{"device_id": "test-device-123", "name": "Test User"}'
```

### 5. Submit Secret Word (Correct)
```bash
curl -X POST http://localhost:8000/api/poi/1/submit/ \
  -H "Content-Type: application/json" \
  -d '{"participant_id": "test-device-123", "secret_word": "Kickstart"}'
```

### 6. Submit Secret Word (Wrong Order - Should Fail)
```bash
curl -X POST http://localhost:8000/api/poi/3/submit/ \
  -H "Content-Type: application/json" \
  -d '{"participant_id": "test-device-123", "secret_word": "SmartHub"}'
```

### 7. Get Game Status
```bash
curl "http://localhost:8000/api/game/status/?device_id=test-device-123"
```

### 8. Check Final Unlock Status
```bash
curl "http://localhost:8000/api/game/final/?device_id=test-device-123"
```

## Complete Game Flow Test

```bash
# 1. Register participant
curl -X POST http://localhost:8000/api/participants/ \
  -H "Content-Type: application/json" \
  -d '{"device_id": "player1", "name": "John Doe"}'

# 2. Submit all POIs in order
curl -X POST http://localhost:8000/api/poi/1/submit/ \
  -H "Content-Type: application/json" \
  -d '{"participant_id": "player1", "secret_word": "Kickstart"}'

curl -X POST http://localhost:8000/api/poi/2/submit/ \
  -H "Content-Type: application/json" \
  -d '{"participant_id": "player1", "secret_word": "Sensors"}'

curl -X POST http://localhost:8000/api/poi/3/submit/ \
  -H "Content-Type: application/json" \
  -d '{"participant_id": "player1", "secret_word": "SmartHub"}'

curl -X POST http://localhost:8000/api/poi/4/submit/ \
  -H "Content-Type: application/json" \
  -d '{"participant_id": "player1", "secret_word": "Compile"}'

curl -X POST http://localhost:8000/api/poi/5/submit/ \
  -H "Content-Type: application/json" \
  -d '{"participant_id": "player1", "secret_word": "Applause"}'

curl -X POST http://localhost:8000/api/poi/6/submit/ \
  -H "Content-Type: application/json" \
  -d '{"participant_id": "player1", "secret_word": "Innovate"}'

# 3. Check final status (should be unlocked)
curl "http://localhost:8000/api/game/final/?device_id=player1"
```
