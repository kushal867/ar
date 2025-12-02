#!/usr/bin/env bash

gunicorn ar_hunt_backend.wsgi:application --bind 0.0.0.0:$PORT --chdir AR_Hunt/backend
