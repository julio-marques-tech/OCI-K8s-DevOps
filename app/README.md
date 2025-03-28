# 📦 Flask Microservice

This directory contains the main Python microservice using [Flask](https://flask.palletsprojects.com/) and [SQLAlchemy](https://www.sqlalchemy.org/) to provide a RESTful API that connects to a PostgreSQL database via Docker Compose.

---

## 🚀 Features

- Lightweight Flask web API  
- CRUD operations for user records  
- SQLAlchemy for ORM and database abstraction  
- Integration with PostgreSQL via Docker network  
- Environment-based configuration

---

## 📁 Project Structure
/Flask │ ├── app/ │ ├── init.py # Flask app factory │ ├── models.py # SQLAlchemy models │ ├── routes.py # CRUD endpoints │ └── config.py # Configuration management │ ├── Dockerfile # Container image for the Flask app ├── requirements.txt # Python dependencies └── .env # Environment variables
---

## 🧪 How to Run Locally

Make sure Docker is installed and running. This service is designed to run with the main `docker-compose.yml` file in the root of the project.

```bash
# 1. Build the Flask image
docker compose build

# 2. Start the Flask and PostgreSQL containers
docker compose up -d

# 3. Check logs to confirm it's running
docker compose logs flask

The Flask API should be available at:
http://localhost:5000/
🔁 API Endpoints
Method	Endpoint	Description
GET	/users	List all users
GET	/users/<id>	Get a user by ID
POST	/users	Create a new user
PUT	/users/<id>	Update user by ID
DELETE	/users/<id>	Delete user by ID
Sample request (POST):

{
  "name": "Alice",
  "email": "alice@example.com"
}
⚙️ Environment Variables
You can configure Flask settings via a .env file or directly in the Docker Compose file.

Example .env:
FLASK_ENV=development
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=flaskdb
POSTGRES_HOST=db

🔍 Test the Application
Once the containers are running, you can test the API using
curl http://localhost:5000/users
Or use Postman or Insomnia for easier testing.

💡 Tips
If changes are made to requirements.txt, rebuild the image with:
docker compose build
The database must be running and accessible for the Flask app to work.

Logs can be viewed with:
docker compose logs flask

🎯 Learning Objectives Covered
✅ Build a RESTful API using Flask

✅ Connect Python service to PostgreSQL using SQLAlchemy

✅ Create and use a Dockerfile for Python microservices

✅ Configure Flask using environment variables

✅ Test endpoints with tools like curl, Postman or Insomnia

📚 References
Flask Documentation

SQLAlchemy ORM

Docker Compose



