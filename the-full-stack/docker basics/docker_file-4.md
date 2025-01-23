# 📑 Dockerfile

A **Dockerfile** is a script that allows you to create custom Docker images. It contains a list of steps that define how the image is built.

---

## ✨ Key Benefits
- **Custom Images**: Build tailored images with everything your app needs.
- **Self-Contained**: No need to mount volumes; the image includes all required files.
- **Reproducibility**: Ensures consistency across environments.

---

## 🚀 Common Dockerfile Commands

### 🔹 `FROM`
- **Purpose**: Specifies the base image for your Docker container.
- **Example**:
  ```docker
  FROM python:3.9-slim
  ```

### 🔹 `WORKDIR`
- **Purpose**: Sets the working directory inside the container.
- **Example**:
  ```docker
  WORKDIR /app
  ```

### 🔹 `COPY`
- **Purpose**: Copies files from your local machine to the container (in app).
- **Example**:
  ```docker
  COPY requirements.txt .
  COPY . .
  ```

### 🔹 `RUN`
- **Purpose**: Executes commands during the build process, such as installing dependencies.
- **Example**:
  ```docker
  RUN pip install --no-cache-dir -r requirements.txt
  ```

### 🔹 `EXPOSE`
- **Purpose**: Declares the port the container will listen on.
- **Example**:
  ```docker
  EXPOSE 5000
  ```

### 🔹 `ENV`
- **Purpose**: Sets environment variables inside the container.
- **Example**:
  ```docker
  ENV FLASK_APP=app.py
  ```

### 🔹 `CMD`
- **Purpose**: Specifies the default command to run when the container starts.
- **Example**:
  ```docker
  CMD ["flask", "run", "--host=0.0.0.0"]
  ```

---

## 📋 Typical Workflow
1. **Start with a Base Image**: Build upon an existing image (e.g., `python:3.9-slim`).
2. **Add Application Files**: Use `COPY` or `ADD` to include your app's code and dependencies.
3. **Install Dependencies**: Use `RUN` to install the necessary packages.
4. **Set Environment Variables**: Define app-specific configurations with `ENV`.
5. **Expose Ports**: Inform Docker which port your app will use via `EXPOSE`.
6. **Define Start Command**: Specify how to start your app using `CMD`.

---

## 🛠 How to Create a Dockerfile
1. **Create a File**: Name it `Dockerfile` in your project's root directory.
2. **Define the Base Image**:
   ```docker
   FROM nginx:latest
   ```
3. **Add Files to the Image or copy it** :
   ```docker
   ADD . /usr/share/nginx/html
   ```
4. **Build the Image**:
   ```bash
   docker build --tag website:latest .
   ```
   - `--tag`: Assigns a name and tag to the image.
   - `website`: The name of your image.
   - `.`: Specifies the context directory (current folder).

---

## 📑DockerfileIgnore
- **Purpose**: Specifies files or directories to ignore when building the Docker image.
- should be in root project directory
- **Example**:
```docker
node_modules
.env
.git
```


## 💡 Tips for Dockerfile Best Practices
- **Keep It Simple**: Use lightweight base images (e.g., `alpine`) when possible.
```docker
FROM nginx:alpine
```
- **Minimize Layers**: Combine related commands to reduce image size.
  ```docker
  RUN apt-get update && apt-get install -y some-package && rm -rf /var/lib/apt/lists/*
  ```
- **Leverage `.dockerignore`**: Exclude unnecessary files from the build context.
- **Use `COPY` Over `ADD`**: Prefer `COPY` for better clarity and control.

---
