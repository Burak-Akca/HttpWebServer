# 🖧 Simple HTTP Server in Python

This project is a minimal HTTP server implemented from scratch using Python's built-in `socket` and `threading` modules. It is designed as a foundational learning exercise in network and system programming.

---

## 🚀 Features

- ✅ **Multi-threaded request handling** (supports multiple simultaneous clients)
- ✅ **Static file serving** (HTML, CSS, JS, images, etc.)
- ✅ **API routing system** (Flask-like handler structure using regex patterns)
- ✅ **Supports `GET` and `POST` methods**
- ✅ **Automatic `Content-Type` detection** (MIME types via `mimetypes` module)
- ✅ **Simple logging** (requests, errors, status codes)
- ✅ **HTTP error handling** (`404 Not Found`, `405 Method Not Allowed`, `500 Internal Server Error`)

---

## 🗂 Project Structure

```
HttpWebServer/
├── server.py          # Main server code
├── static/            # Static files (HTML, CSS, JS, images)
│   ├── index.html
│   ├── style.css
│   └── script.js
```

> Note: Everything can also be bundled inside a single `server.py` file if desired.

---

## 🧪 Sample Endpoints

### Static Files
- `GET /static/index.html` → Returns `index.html` from the `static/` folder
- `GET /static/style.css` → Returns `style.css`

### API Endpoints
- `GET /api/hello`  
  Returns a JSON response:  
  ```json
  { "message": "Merhaba Dünya!" }
  ```

- `GET /user/<id>`  
  Returns mock user info with the given ID.

- `POST /user/<id>`  
  Accepts a JSON body and returns it with the user ID.

---

## 🏁 Running the Server

```bash
python server.py
```

Then, open your browser and navigate to:

```
http://localhost:8080/static/index.html
http://localhost:8080/api/hello
http://localhost:8080/user/123
```

---

## 📦 Docker Support

You can build and run this server inside a Docker container:

**Dockerfile:**
```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8080

CMD ["python", "server.py"]
```

**Build and run:**
```bash
docker build -t my-http-server .
docker run -p 8080:8080 my-http-server
```

---

## 📚 Learning Goals

This project was designed to demonstrate:

- Low-level HTTP protocol understanding
- Manual request parsing and routing
- Concurrency with threading
- Basic file and MIME handling
- Docker-based deployment
- Minimalist architecture without using frameworks

---

## ⚠️ Limitations

- No TLS (HTTPS)
- No form handling (only raw JSON POST)
- No persistent database or session management

---

## 📄 License

MIT License © 2025