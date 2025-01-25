# 📑 Deployment Guide

Deployment is the process of uploading your application to a server and making it available to users.

---

## 🌐 Types of Deployment
1. **Server (Manual)**
2. **Serverless (Automatic)**

---

## 1️⃣ Server Deployment (Manual)
- **What is it?**
  - A physical or virtual machine hosting your application.
- **How to do it?**
  - Manually upload files using tools like:
    - 🛠️ `FTP` / `SFTP`
    - 🔄 `rsync`
- **When to use?**
  - High resource requirements ⚡
  - High traffic 🌐
  - Advanced customization 🔧
  - High-level security requirements 🔒

---

## 2️⃣ Serverless Deployment (Automatic)
- **What is it?**
  - Starts when developers push changes to version control systems like `GitHub`.
- **How it works?**
  1. Automatically generate a build environment identical to production.
  2. Run the build process: `test` ➡️ `build` ➡️ `deploy`.
  3. Automatically manage memory and scaling.
- **When to use?**
  - Low traffic websites 🧑‍💻
  - Simple functionality ✅
  - Flexible requirements 🔄

---

## 🤝 CI/CD: Continuous Integration and Deployment

### 🛠️ Continuous Integration (CI)
- Simulates the development environment and runs tests to ensure code quality.

### 🚀 Continuous Deployment/Delivery (CD)
- Automatically deploys your application after passing tests.

---

## 🔄 CI/CD Workflow
1. **Code** ✍️
2. **Version Control** 📂
3. **Build** 🏗️
4. **Test** ✅
5. **Deploy** 🚀

---

## 🔧 Useful Tools for CI/CD
- **Jenkins** 🤖
- **Travis CI** 🛠️
- **Circle CI** 🔄
- **GitLab CI/CD** 🛡️
- **GitHub Actions** ⚡

---

### 💡 Note
If tests are skipped, the process is called `CD` (Continuous Deployment): 
`Code` ➡️ `Version Control` ➡️ `Deploy`

