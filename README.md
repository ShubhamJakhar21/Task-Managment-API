# 📌 Task Management API

**FastAPI · PostgreSQL · Docker**

A production-style RESTful API for managing tasks with full CRUD functionality. This project demonstrates backend development using FastAPI, PostgreSQL, and Docker with clean architecture and containerized deployment.

📄 Detailed Build Guide: 

---

## 🚀 Features

* Create, Read, Update, Delete (CRUD) tasks
* PostgreSQL relational database
* Pydantic data validation
* Auto-generated Swagger & ReDoc documentation
* Dockerized multi-container setup
* Status-based task filtering

---

## 🛠 Tech Stack

* **Python 3.11**
* **FastAPI**
* **PostgreSQL**
* **Pydantic**
* **psycopg2**
* **Docker & Docker Compose**
* **Postman (API Testing)**

---

## 📁 Project Structure

```
task-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   └── routes/
│       └── tasks.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/task-management-api.git
cd task-management-api
```

### 2️⃣ Run with Docker

```bash
docker compose up --build
```

Application runs at:

```
http://localhost:8000
```

Swagger Docs:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

## 📌 API Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| POST   | /tasks/     | Create a task  |
| GET    | /tasks/     | Get all tasks  |
| GET    | /tasks/{id} | Get task by ID |
| PUT    | /tasks/{id} | Update task    |
| DELETE | /tasks/{id} | Delete task    |

### Example Request (Create Task)

```json
{
  "title": "Learn FastAPI",
  "description": "Build a task API",
  "status": "in_progress"
}
```

---

## 🐳 Docker Services

* **db** → PostgreSQL container
* **api** → FastAPI application container

Run in background:

```bash
docker compose up -d --build
```

Stop services:

```bash
docker compose down
```

---

## 🧪 Testing

You can test endpoints using:

* Swagger UI (`/docs`)
* ReDoc (`/redoc`)
* Postman

---

## 🔍 Troubleshooting

* Port already in use → Change port in `docker-compose.yml`
* DB connection issue → Restart API container
* Reset DB → `docker compose down -v`

---

## 📈 Future Improvements

* Authentication & JWT
* User-based task ownership
* Pagination
* Logging & monitoring
* CI/CD integration

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

### ⭐ If you found this helpful, consider giving it a star!

