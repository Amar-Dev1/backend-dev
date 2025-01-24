# Dockerfile Layer Caching 🐳⚡

Learn how to use Docker's layer caching to speed up builds! 🚀

---

## **Key Concept** 🧠

Docker caches each layer (instruction) in the Dockerfile. If a layer hasn’t changed, Docker reuses the cached layer instead of rebuilding it. 🔄

---

## **Example Dockerfile with Caching** 🛠️

### Directory Structure 📂
```txt

my_flask_app/
├── app.py
├── requirements.txt
└── Dockerfile
```

### Dockerfile 🐋
```Dockerfile
# Step 1: Use a base image
FROM python:3.12-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy requirements.txt first (to leverage caching)
COPY requirements.txt .

# Step 4: Install dependencies (cached if requirements.txt doesn’t change)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code (cached if code doesn’t change)
COPY . .

# Step 6: Expose the port
EXPOSE 5000

# Step 7: Set environment variables
ENV FLASK_APP=app.py

# Step 8: Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
```
## How Caching Works 🔄
### 1. `COPY requirements.txt .`
- Cached if requirements.txt doesn’t change. 📄
### 2. `RUN pip install`
- Cached if requirements.txt doesn’t change. 📦
### 3. `COPY . .`
- Cached if application code doesn’t change. 📁
### 4 . `Subsequent Layers`
- If any layer changes, all subsequent layers are rebuilt. 🔄

## Best Practices 🏆
### 1. Order Instructions ⬇️
- Place less frequently changed instructions (e.g., `COPY requirements.txt`) before frequently changed ones (e.g., `COPY . .`).
### 2. Use `.dockerignore` 🚫
- Exclude unnecessary files (e.g., `__pycache__`, `.git`) to avoid cache invalidation.