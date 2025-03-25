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
✅ Lab Status
 Flask API + PostgreSQL containerized

 Tested locally with Docker Compose

 Deployed on OCI

 CI/CD pipeline in GitHub Actions

 Infrastructure provisioned with Terraform

 Ansible automation

 Full documentation and diagrams

🛠️ Technologies & Tools
Tool	Purpose
Flask	Backend API (Python microservice)
PostgreSQL	Relational database
Docker	Containerization
Docker Compose	Multi-container orchestration
Kubernetes	Production-grade container orchestration
Terraform	Infrastructure as Code (IaC)
GitHub Actions	CI/CD pipelines
Ansible	Provisioning and configuration management
Oracle Cloud	Cloud deployment target
🧠 Learning Objectives
Gain fluency in cloud-native DevOps tools

Understand microservices, containers, and networking

Apply CI/CD concepts in real pipelines

Learn and apply Infrastructure as Code (IaC)

Integrate with Oracle Cloud and Salesforce

🧪 Run Locally (API + DB in Docker)
bash
Copiar
Editar
# Clone the repository
git clone https://github.com/julio-marques-tech/OCI-K8s-DevOps.git
cd OCI-K8s-DevOps/docker

# Start the containers
docker-compose up --build -d

# Test the Flask API
curl http://localhost:5000/               # GET - check API
curl http://localhost:5000/users          # GET - list users
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Julio", "email": "julio@example.com"}'
🤝 Contributing
This repository is part of my personal study lab but also open to the community. Feel free to fork, test, submit issues or pull requests. Let’s grow together. 🌱

📄 License
MIT License

🧭 Final Notes
Stay tuned! I’ll be updating this repository as I go through my certifications, expand my cloud skills, and build real-world experience — always sharing the journey. 🌍
