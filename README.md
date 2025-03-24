# 🐳 Docker - Containerization Lab

This directory contains the Docker setup for the Flask + PostgreSQL microservice used throughout this DevOps Lab. It includes the Dockerfile, Docker Compose file, and supporting configuration for a local development environment.

---

## 📦 Project Components

- **Flask API** container
- **PostgreSQL** database container
- Gunicorn server for production-ready Flask

---

## 🛠️ Files and Purpose

- `Dockerfile`: Builds the Flask app image using Python 3.12
- `docker-compose.yml`: Orchestrates Flask + PostgreSQL containers
- `requirements.txt`: Python dependencies
- `README.md`: This file with setup and explanations

---

## 🚀 How to Build and Run

```bash
# 1. Build and start containers
docker-compose up --build -d

# 2. Check running containers
docker ps

# 3. Stop and remove all containers, volumes, and networks
docker-compose down -v

