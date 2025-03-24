# 🐳 Docker Setup

This folder contains the Docker configuration for running a Flask API connected to a PostgreSQL database using `docker-compose`.

It serves as the foundation for containerization within the OCI-K8s-DevOps lab, helping simulate a production-ready environment.

---

## 📁 Structure

docker/ ├── Dockerfile # Defines the Flask app image ├── docker-compose.yml # Sets up Flask + PostgreSQL services └── README.md # You are here

markdown
Copiar
Editar

---

## ⚙️ Dockerfile Summary

- Uses the official Python 3.12 image
- Creates `/app` as the working directory
- Installs Python dependencies via `requirements.txt`
- Copies Flask project code into container
- Exposes port `5000`
- Runs the app with `gunicorn`

```dockerfile
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]
🔄 docker-compose.yml Summary
Service: app

Builds the image from the Dockerfile

Depends on the db service

Maps port 5000 to localhost

Service: db

Uses the official postgres:15 image

Sets up a database named mydatabase

🚀 Run Locally
Make sure you're in the docker/ directory:

bash
Copiar
Editar
cd docker
Then build and run everything:

bash
Copiar
Editar
docker-compose up --build -d
✅ Test the API
Use curl to test your Flask API locally:

bash
Copiar
Editar
curl http://localhost:5000/                     # Health check
curl http://localhost:5000/users                # GET all users
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Julio", "email": "julio@example.com"}'
🧠 Concepts Practiced
Dockerfile structure and build

Docker Compose for multi-container apps

Flask and PostgreSQL integration

Container networking

Volume persistence for database

🐛 Troubleshooting
If something breaks:

bash
Copiar
Editar
docker-compose down
docker system prune -f
docker-compose up --build -d
🧹 Cleanup
To stop and remove all containers:

bash
Copiar
Editar
docker-compose down
To remove unused images, volumes, and networks:

bash
Copiar
Editar
docker system prune -f
