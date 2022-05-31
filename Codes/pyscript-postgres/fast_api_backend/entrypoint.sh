#!/bin/sh

echo "Running FastAPI Server"
uvicorn backend:app --reload --workers 1 --host 0.0.0.0 --port 8000
