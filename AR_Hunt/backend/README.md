# AR Campus Hunt - Django Backend

A Django REST Framework backend for the AR Campus Hunt game at Virinchi College.

## Features

- **POI Management**: 6 checkpoints across campus
- **Sequence Enforcement**: Players must complete POIs in order
- **Progress Tracking**: Real-time tracking of participant progress
- **QR Code Generation**: Dynamic QR codes for each POI
- **Admin Interface**: Django admin for managing game data

## Quick Start

### 1. Install Dependencies
```bash
cd backend
pip install django djangorestframework django-cors-headers
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Seed POI Data
```bash
python manage.py seed_pois
```

### 4. Create Admin User
```bash
python manage.py createsuperuser
```

### 5. Start Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

### POI Endpoints
- `GET /api/poi/` - List all POIs
- `GET /api/poi/<id>/` - Get POI details
- `GET /api/poi/<id>/qr/` - Get QR code for POI
- `POST /api/poi/<id>/submit/` - Submit secret word

### Participant Endpoints
- `POST /api/participants/` - Register new participant
- `GET /api/participants/<device_id>/` - Get participant details

### Game Status
- `GET /api/game/status/?device_id=<id>` - Get participant progress
- `GET /api/game/final/?device_id=<id>` - Check if final form is unlocked

## Game Flow

1. **Register**: Frontend creates participant with unique device_id
2. **Get POIs**: Fetch list of all POIs
3. **Scan QR**: Get QR code for current POI
4. **Submit Word**: Submit secret word for POI
5. **Progress**: Backend validates sequence and word
6. **Repeat**: Continue until all 6 POIs completed
7. **Final**: Access final submission form

## Admin Panel

Access at `http://localhost:8000/admin/`

Default credentials:
- Username: `admin`
- Password: (set during createsuperuser)

## POI Data

| Order | Name | Secret Word | Icon |
|-------|------|-------------|------|
| 1 | Main Entrance | Kickstart | 🚪 |
| 2 | Robo Soccer Zone | Sensors | 🤖 |
| 3 | IoT Project Exhibition | SmartHub | 💡 |
| 4 | Library | Compile | 📚 |
| 5 | Computer Lab | Applause | 💻 |
| 6 | Main Stage (Final) | Innovate | 🎯 |

## Testing

See [API_TESTING.md](./API_TESTING.md) for detailed API testing examples.

## Configuration

### CORS Settings
Currently set to allow all origins for development. Update in `settings.py` for production:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://yourdomain.com"
]
```

### Database
Using SQLite for development. For production, configure PostgreSQL in `settings.py`.

## Project Structure

```
backend/
├── ar_hunt_backend/     # Django project settings
│   ├── settings.py
│   └── urls.py
├── game/                # Main game app
│   ├── models.py        # POI, Participant, Progress models
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # API viewsets
│   ├── admin.py         # Admin configuration
│   └── management/
│       └── commands/
│           └── seed_pois.py
├── manage.py
└── db.sqlite3
```
