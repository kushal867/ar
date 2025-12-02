#!/bin/bash
# Start Django backend server on all network interfaces
# This allows access from localhost, 192.168.0.104, and any other IP

echo "🚀 Starting Django Backend Server..."
echo "📡 Server will be accessible from:"
echo "   - http://localhost:8000"
echo "   - http://127.0.0.1:8000"
echo "   - http://192.168.0.104:8000"
echo "   - http://<any-network-ip>:8000"
echo ""

cd "$(dirname "$0")"
python manage.py runserver 0.0.0.0:8000
