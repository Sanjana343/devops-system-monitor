# DevOps System Monitor API

A lightweight Flask-based monitoring API that exposes system CPU and memory metrics.

## Features
- REST API using Flask
- Real-time CPU monitoring
- Real-time Memory monitoring
- Git version control

## Endpoints

GET /

GET /health

## Run Locally

python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
python3 app.py