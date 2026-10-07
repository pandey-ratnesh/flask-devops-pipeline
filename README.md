# Containerized Python API with CI/CD Pipeline

![CI/CD Status](https://github.com/pandey-ratnesh/flask-devops-pipeline/actions/workflows/ci-cd.yml/badge.svg)

## Overview
A lightweight, production-ready Flask REST API containerized with Docker and Docker Compose, equipped with an automated CI/CD pipeline using GitHub Actions to enforce code quality, run automated tests, and deliver images to Docker Hub.

## Tech Stack
* **Language & Framework:** Python 3.11, Flask
* **Server:** Gunicorn (Production WSGI)
* **Testing & Linting:** Pytest, Flake8
* **Containerization:** Docker, Docker Compose
* **CI/CD:** GitHub Actions
* **Registry:** Docker Hub

## Architecture & CI/CD Flow
1. Developer pushes code to `main`.
2. **GitHub Actions Trigger:**
   * **Job 1 (Test):** Executes Flake8 for PEP 8 enforcement and Pytest for unit testing.
   * **Job 2 (Build & Push):** Uses Docker Buildx and GitHub layer caching to build multi-platform production containers and push tagged images (`:latest` and short commit SHA) to Docker Hub.

## Local Development

### 1. Run via Docker Compose
```bash
docker compose up --build -d
curl http://localhost:5000/

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/
flake8 app/ tests/ --max-line-length=120

docker pull ratneshpandey/flask-devops-api:latest
docker run -d -p 5000:5000 ratneshpandey/flask-devops-api:latest

