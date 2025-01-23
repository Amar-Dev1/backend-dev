# 📑 Volumes

- A volume can be either a file or a folder.
- Volumes allow sharing data between the **host** (machine) and **container** and also between **containers**.
- Volumes can be mounted on multiple **hosts** (machines).
- They are used to share data between different applications.

## 📑 Volume Between **Host** and **Containers**

- The **host** can mount a volume to a **container**.
- The **container** can mount a volume from the **host**.
- Example: Assume you created a file called `index.html` on your **host** (machine).
  
### Mounting the File from **Host** to **Container**

You can mount this file to your container by running:

```bash
docker run --name website -v $(dir):/usr/share/nginx/html:ro -d -p 8080:80 nginx
```

- `$(dir)` is the path to the file `index.html` in your **host**.
- `ro` stands for **read-only**.

## 💡 Notes

- If you have a file inside the **container**, that will also appear in your **host**.
- To access the container in interactive mode, run the command:
  
  ```bash
  docker exec -it <container_name> bash
  ```
  
- Once inside the container, navigate to the mounted volume:
  
  ```bash
  cd /usr/share/nginx/html
  ls -al
  ```
  
- To add a file inside the container, use the following command:
  
  ```bash
  touch about.html
  ```
  
This will create a file `about.html` inside the container, and if the volume is correctly mounted, the file will appear on your host system as well.

## 📑Sharing volumes between **containers**
- we can use `--volume-from <container_name>`
- assume we have container: `website`
- we can share the volume between it and another by running:
```bash
docker run --name website-copy --volume-from website -d -p 8081:80 nginx
```
- This will create a new container `website-copy` and share the volume from `website` container