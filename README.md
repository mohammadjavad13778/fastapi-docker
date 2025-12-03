# 🚀 FastAPI + Docker

[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.10+-yellow?logo=python)](https://www.python.org/)

---

## 📖 Overview
This repository contains a **basic FastAPI application** packaged with a Dockerfile.  
It serves as a clean starting point for building APIs with FastAPI and deploying them in Docker environments.

---

## 📂 Project Structure
fastapi-docker/ 
│── Basicfastapi/ # FastAPI application code 
│── Dockerfile # Docker build instructions 
│── requirements.txt # Dependencies 
│── README.md # Documentation

---
⚙️ Setup & Usage
🔨 Build the Docker image

docker build -t fastapi-docker-app .

▶️ Run the container
docker run --rm -it -p 8000:8000 fastapi-docker-app

🧪 Testing
You can test endpoints using curl or any API client (e.g., Postman, HTTPie).

Example:
curl http://localhost:8000/items/1?q=hello




CMD ["uvicorn", "Basicfastapi.app:app", "--host", "0.0.0.0", "--port", "8000"]

