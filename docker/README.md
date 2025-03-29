# 🐳 Docker Setup

This folder contains the Docker configuration for running a Flask API connected to a PostgreSQL database using Docker Compose.

It serves as the foundation for containerization within the **OCI-K8s-DevOps** lab, helping simulate a production-ready environment that is ready to scale with Kubernetes, CI/CD, OCI, and cloud-native tools.

---

## 📁 Structure

/docker │ ├── Dockerfile # Defines the Flask app image ├── docker-compose.yml # Sets up Flask + PostgreSQL services └── README.md # You are here

---

## ⚙️ Dockerfile Summary

- Uses the official Python 3.12 image  
- Creates `/app` as the working directory  
- Installs Python dependencies via `requirements.txt`  
- Copies Flask project code into the container  
- Exposes port 5000  
- Runs the app with Gunicorn:

```dockerfile
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]
🔄 docker-compose.yml Summary
Service: app
Builds the image from the Dockerfile

Depends on the db service

Maps port 5000 to localhost

Service: db
Uses the official postgres:15 image

Sets up a database named flaskdb

Connected via Docker Compose service name db

🚀 Run Locally
Make sure you're in the /docker directory:

bash
Copiar
Editar
cd docker
Then build and run everything:

bash
Copiar
Editar
docker-compose up --build -d
```
---
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
  ---
🧠 Concepts Practiced
Dockerfile structure and build

Docker Compose for multi-container applications

Flask and PostgreSQL integration

Container networking

Volume persistence for PostgreSQL

Foundation for Kubernetes deployments

Ready for CI/CD pipelines using GitHub Actions

Future integrations with Slack, Salesforce, and OCI
---
🐛 Troubleshooting
If something breaks:

bash
Copiar
Editar
docker-compose down
docker system prune -f
docker-compose up --build -d
---
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
---
🔮 Ready for the Future
This structure is ready to support:

Kubernetes manifests using this Docker image

CI/CD with GitHub Actions using this Dockerfile

Container deployment to Oracle Cloud (OCI)

Monitoring/log forwarding to Slack or Salesforce

Dynamic scaling and orchestration in a DevOps workflow
---
📚 References
Dockerfile Best Practices

Docker Compose Docs

Gunicorn Docs
```
