# 🗄️ PostgreSQL Database (Docker)

This directory contains the configuration for the PostgreSQL container used by the Flask microservice.

The database is managed using Docker and is automatically linked via Docker Compose to the Flask app using the service name `db`.

---

## 🧱 Features

- PostgreSQL running in a Docker container  
- Persistent volume (optional)  
- Pre-configured environment variables for seamless integration with Flask  
- Designed to be used with `docker-compose.yml`

---

## 📁 Project Structure

```markdown
/db
│
├── init.sql               # (Optional) Initial SQL setup script
├── Dockerfile             # Custom image (if needed)
└── .env                   # PostgreSQL environment variables (user, password, db)
⚙️ Environment Variables
These are typically defined in the .env file and referenced in docker-compose.yml.

Example .env:

ini
Copiar
Editar
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=flaskdb
You can also set these directly in docker-compose.yml.

🚀 How to Run
The database runs as part of the main docker-compose workflow:

bash
Copiar
Editar
docker compose up -d
To inspect logs:

bash
Copiar
Editar
docker compose logs db
To connect manually:

bash
Copiar
Editar
docker exec -it <container_name_or_id> psql -U postgres -d flaskdb
Example:

bash
Copiar
Editar
docker exec -it oci-k8s-devops-db-1 psql -U postgres -d flaskdb
🧪 Testing the Connection
Once running, test connection from host:

bash
Copiar
Editar
# Basic port test (if port is exposed)
telnet localhost 5432
Or test inside the Flask container (if installed):

bash
Copiar
Editar
psql -h db -U postgres -d flaskdb
🔐 Data Persistence (Optional)
If using a volume for data persistence, add this to your docker-compose.yml:

yaml
Copiar
Editar
volumes:
  - pgdata:/var/lib/postgresql/data

# And define the volume
volumes:
  pgdata:
🎯 Learning Objectives Covered
✅ Run PostgreSQL using Docker

✅ Configure database with environment variables

✅ Link PostgreSQL to another container (Flask) via service name

✅ Inspect, connect and test PostgreSQL in container

📚 References
PostgreSQL Docs

Docker Hub - postgres

Docker Compose Networking
