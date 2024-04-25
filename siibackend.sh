#!/bin/bash
source /home/siiuser/NUL-SII-site-backend/venv/bin/activate
exec uvicorn nul_sii_site.asgi:application --host 127.0.0.1 --port 8002 --workers 5