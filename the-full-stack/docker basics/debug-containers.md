# 📑 Debugging Docker Containers

Debugging Docker containers is a crucial skill for identifying and resolving issues effectively. Below are some essential tools and commands to help you debug like a pro! 🚀

---

## 📑 Docker Inspect 🕵️‍♂️
The `docker inspect` command provides detailed information about a container in `JSON` format. This is useful for understanding the container's state, configuration, and network settings.

### 📌 Usage:
```bash
docker inspect <container_id> or <container_name>
```

### 🎯 What You Can Learn:
- **Container Configuration**: Environment variables, mounts, and entry points.
- **State Information**: Whether the container is running, paused, or stopped.
- **Network Details**: IP address, ports, and network mode.

### 🛠️ Example:
```bash
docker inspect my_container
```
---

## 📑 Docker Logs 📜
The `docker logs` command is vital for checking the output of your container's processes. This helps diagnose issues by viewing application logs.

### 📌 Usage:
```bash
docker logs <container_id> or <container_name>
```

### 🎯 Options:
- `--tail <number>`: Show only the last `<number>` of log lines.
- `-f`: Follow logs in real-time (like `tail -f`).
- `--since <time>`: Show logs since a specific time.

### 🛠️ Example:
```bash
# View last 10 log lines
docker logs --tail 10 my_container

# Follow logs in real-time
docker logs -f my_container
```
---

## 📑 Docker Exec 🛠️
The `docker exec` command lets you run a command directly inside a running container. This is helpful for debugging by interacting with the container's environment.

### 📌 Usage:
```bash
docker exec -it <container_id> or <container_name> <command>
```

### 🎯 Key Options:
- `-i`: Keep STDIN open.
- `-t`: Allocate a pseudo-TTY for an interactive session.

### 🛠️ Example:
```bash
# Start a Bash shell inside the container
docker exec -it my_container /bin/bash

# Check running processes
docker exec -it my_container ps aux
```
---

## 🔍 Additional Tips:
1. **Check Running Containers**:
   ```bash
   docker ps
   ```
   Lists all running containers with their names and IDs.

2. **Inspect Networks**:
   ```bash
   docker network inspect <network_name>
   ```
   View network details to debug connectivity issues.

3. **Use Docker Stats**:
   ```bash
   docker stats
   ```
   Monitor container resource usage (CPU, memory, network, etc.).

4. **Check Container Events**:
   ```bash
   docker events
   ```
   Stream real-time events from the Docker daemon.

---

Debugging Docker containers becomes easier with these tools and commands at your fingertips. Happy debugging! 🐳
