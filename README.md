# 🚀 OCI-K8s-DevOps Lab

This repository is a hands-on study lab designed to consolidate and demonstrate my understanding of key **DevOps** concepts through practical application.

The tech stack includes:

- Docker
- Kubernetes
- Terraform
- CI/CD with GitHub Actions
- Flask (Python)
- Ansible

> 📌 All examples are real-world oriented, and the content is structured to help others in the community who want to **learn by doing**.

---

## 🎯 Project Goal

To create a complete DevOps lab that:

- Builds and runs a containerized **Flask API** application with **PostgreSQL**
- Deploys the setup to **Oracle Cloud Infrastructure (OCI)**
- Automates infrastructure provisioning using **Terraform**
- Implements **CI/CD pipelines** via GitHub Actions
- Applies **Ansible** for configuration management
- Documents each step clearly for learning and sharing with the community

---

## 📁 Repository Structure

```bash
.
├── Docker/         # Dockerfiles, docker-compose, API + DB setup
├── Kubernetes/     # K8s manifests (YAMLs) for deployment
├── Terraform/      # IaC for provisioning OCI infrastructure
├── CI-CD/          # GitHub Actions workflows
├── Flask/          # Flask application (CRUD + PostgreSQL)
├── Ansible/        # Playbooks for provisioning/configuration
├── db/             # SQL scripts for database setup
├── docs/           # Markdown files with guides, architecture, diagrams
└── README.md       # Overview and instructions (this file)
---

✅ Lab Status
To keep track of the lab's progress:

✅ Flask API + PostgreSQL containerized

✅ Tested locally with Docker Compose

🔄 Deployment on Oracle Cloud Infrastructure (OCI)

🔄 CI/CD pipeline configured via GitHub Actions

🔄 Infrastructure provisioning with Terraform

🔄 Configuration automation with Ansible

📚 Full documentation with guides, diagrams and instructions

🛠️ Technologies & Tools
Tools and technologies used in this lab:

Flask (Python) – Microservice for the API

PostgreSQL – Relational database

Docker & Docker Compose – Containerization

Kubernetes – Orchestration of containers

Terraform – Infrastructure as Code (IaC)

GitHub Actions – CI/CD pipeline automation

Ansible – Configuration management

Oracle Cloud Infrastructure (OCI) – Cloud provider target

🧠 Learning Objectives
Main goals behind the lab:

Develop fluency with cloud-native DevOps tools

Understand containers, microservices, networking, and orchestration

Create and maintain real-world CI/CD pipelines

Apply IaC principles using Terraform

Integrate OCI knowledge with Salesforce and Trailhead studies

Build a portfolio-worthy project, helping others in the tech community

🧪 Run Locally (Docker Compose)
bash
Copiar
Editar
# Clone the repo
git clone https://github.com/julio-marques-tech/OCI-K8s-DevOps.git
cd OCI-K8s-DevOps/docker

# Start the containers
docker-compose up --build -d

# Test the API
curl http://localhost:5000/               # GET - API check
curl http://localhost:5000/users          # GET - fetch all users
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Julio", "email": "julio@example.com"}'
🤝 Contributing
This project is not only for personal learning but also to help others in the community.
Feel free to:

Fork the repo

Suggest improvements

Open issues or PRs

Share with other learners 🚀

📄 License
Distributed under the MIT License.
See LICENSE for more information.
