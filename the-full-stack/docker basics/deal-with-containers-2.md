# 📑 Dealing with Containers

- 💡 To use containers, you need an **image**.
- 💡 You can find many images from **docker registries** like **Docker Hub**.

## 💡 Registry
- **Docker registry**: A central location provided by **Docker Hub**, used for storing and sharing container images.
- **Docker Hub**: A popular container registry offering free and paid plans for storing and sharing images. You can download images from it.

## 1️⃣ Pull Images
- **docker pull**: A command to download an image from a registry.
```bash
docker pull nginx:latest
```
  - `nginx`: An image.
  - `:latest`: Refers to the latest version of the image.
  - `docker pull`: Downloads the latest version of the image from the registry.

## 2️⃣ Run the Container
- **docker run**: A command to start a container from an image.
```bash
docker run nginx:latest
```
- To run in **detached mode**, add `-d`.
```bash
docker run -d nginx:latest
```

## 3️⃣ Using the Container
- Assume the `tcp` port is `80` (`80/tcp`).
- Add any localhost port you want with `-p <your localhost>:80`.
- For example, mapping `localhost:8080` to port `80` on the container:
```bash
docker run -d -p 8080:80 nginx:latest
```
- Now you can access the container project in your browser at `localhost:8080`.

### 💡 Notes
- You can expose multiple ports:
```bash
docker run -d -p 8080:80 -p 8081:81 nginx:latest
```

## 👑 Managing Containers (Stop, Remove, Start, and Name Containers)

### 1️⃣ To Stop a Container
```bash
docker stop <container id> or <container name>
```

### 2️⃣ To Remove a Container
```bash
docker rm <container id> or <container name>
```
- To remove all containers in one command:
```bash
docker rm $(docker ps -aq)
```
- ❗ You cannot remove a running container unless you force it using `-f`.

## 📂 Naming Containers
- Instead of random names, you can name your container using `--name`.
```bash
docker run -d --name mynginx nginx:latest
```

## 📏 Formatting Docker ps
- You can format the output of `docker ps` for better readability by adding `--format`:
```bash
docker ps -a --format="{{.ID}}\n{{.Image}}\n{{.Name}}\n{{.Status}}\n{{.Ports}}"
```

