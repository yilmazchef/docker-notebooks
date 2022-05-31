#!/bin/sh

echo "Running Bottle Server"
python backend.py
# uvicorn backend:app --reload --workers 1 --host 0.0.0.0 --port 8080
