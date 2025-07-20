# Command_Cloud - Dockerized Web CTF Challenge

This repository contains a Flask-based web CTF challenge that dynamically launches user-specific Docker containers, each mapped to a unique port. It also includes a TCP server (`server.py`) that participants can connect to in order to trigger container creation and get challenge URLs.

---

## 🐳 Docker Environment

### Base Image
- `python:3.11-slim`

### Installed tools
- `curl`, `ping` (via `apt`)
- Flask and other dependencies from `requirements.txt`

---

## 📁 Project Structure

Command_Cloud/
├── app.py # Flask app (entry point)
├── server.py # TCP CTF server (listens on port 9999)
├── Dockerfile # Docker build file for challenge image
├── requirements.txt # Python dependencies
├── static/ # Flask static files
└── templates/ # Flask HTML templates


---

## 🚀 How it works

- A TCP server (`server.py`) listens on **port 9999**.
- When a participant connects and enters a username, a Docker container is started:
  - Container name: `webctf_<username>`
  - Port: `10000 + (base36(last 2 chars of username) % 1000)`
- Each container serves the Flask app at:



---

## ⚙️ Usage

### 1. Build Docker Image

```bash
docker build -t create_cc .
docker run -d -p 5000:5000 --network host create_cc

screen -S my_ctf_web
python3 server.py

Ctrl + A D

nc <EC2-IP> 9999
