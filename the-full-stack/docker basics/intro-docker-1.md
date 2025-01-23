# 🚢 Docker

- 💡 Docker is a tool that allows you to run applications in isolated environments, called **containers**. 🌐

---

## 🛠️ What is Docker?
- Docker provides lightweight, portable containers for application deployment.
- Similar to virtual environments, but **faster** and **more efficient**.
- Uses **base images** to create isolated environments.

---

## 📦 Containers
- **Containers** are:
  - Lightweight and portable 🛠️
  - Isolated environments sharing the host OS 🖥️
  - Created from **base images** with all necessary dependencies.
- **Advantages:**
  - Easy to create, start, stop, and delete.
  - Ideal for deploying consistent environments across machines. 🚀

---

## ⚙️ Common Docker Commands
💡 Use `docker` in the **CLI** to see all commands.

### 🔧 Container Management
- `docker run <image>`: Start a container from an image ▶️
- `docker ps`: List only the running containers 📋
- `docker stop <container>`: Stop a running container ⛔
- `docker rm <container>`: Remove a container 🗑️
- `docker exec <container> <command>`: Run commands in a container 🖋️
- `docker logs <container>`: View container logs 📝

### 📦 Image Management
- `docker images`: List available images 📋
- `docker pull <image>`: Download an image from a registry ⬇️
- `docker push <image>`: Upload an image to a registry ⬆️
- `docker inspect <name>`: Inspect a container/image 🔍

---

## 🖼️ Docker Images
- **What is a Docker Image?**
  - A **template** containing:
    - Operating system 🖥️
    - Software 🛠️
    - Application code 📜
  - Used to create containers 🚀.

- **Key Feature:**
  - **Versioning:** Create multiple snapshots and revert to any version anytime! 🕒

---

## 💡 Docker Workflow
1️⃣ Start with a **Docker Image**. 🖼️  
2️⃣ Use the image to create and run a **Docker Container**. 🧱  

---

💡 **Tip:** Docker can be used with:
- **CLI (Command-Line Interface)**: Primary interaction tool.
- **Docker Desktop (GUI)**: Must be running for the CLI to work.

## 📑Push workflow
```bash
# Build the image
docker build -t image .

# Tag the image
docker tag my-flask-app myusername/image

# Log in to Docker Hub
docker login

# Push the image
docker push myusername/image
```
- 💡the image should be with its version