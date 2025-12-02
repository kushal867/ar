#!/usr/bin/env bash

cd AR_Hunt/backend
gunicorn ar_hunt_backend.wsgi:application --bind 0.0.0.0:$PORT
