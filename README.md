# Task Manager Flask App

A simple Task Manager web application built with **Flask** and **MongoDB**, containerized with **Docker**.  
Users can **add**, **view**, **mark complete**, and **delete** tasks via a RESTful API and a clean, minimal UI.

---

## 🚀 Features

- Add new tasks with title and status
- View all tasks in a list
- Mark tasks as completed (with strike-through)
- Delete tasks by clicking the ❌ button
- Backend REST API built with Flask and MongoDB
- Simple, interactive UI with vanilla JavaScript
- Containerized with Docker and Docker Compose for easy deployment

---

## 🧰 Tech Stack

- Python 3.11 with Flask
- MongoDB (using pymongo driver)
- Docker & Docker Compose
- Vanilla JavaScript, HTML, and CSS for frontend

---



## ⚙️ How to Run Locally

1. Clone the repo:

   ```bash
   git clone <repo-url>
   cd task-manager ```
   
Build and run with Docker Compose:

```bash docker-compose up --build ```

Open your browser at:
```bash http://localhost:5000 ```

🐳 Docker Commands
 Build image locally:
```bash
docker build -t <monika413>/task-manager-flask-app .
Run container locally:
docker run -p 5000:5000 <your-dockerhub-username>/task-manager-flask-app
```
Push image to Docker Hub:
```bash docker push monika413/task-manager-flask-app ```

📝 API Endpoints

| Endpoint                 | Method | Description               |
|--------------------------|--------|---------------------------|
| /tasks                   | GET    | Get list of all tasks     |
| /tasks                   | POST   | Add a new task            |
| /tasks/<task_id>         | DELETE | Delete a task by ID       |
| /tasks/<task_id>/done    | PATCH  | Mark a task as completed  |


🔧 Environment Variables
```bash MONGO_URI - MongoDB connection string (default: mongodb://localhost:27017/) ```

👤 Author
 Monika Kumari

Docker Hub Image: monika413/task-manager-flask-app

Feel free to open issues or contribute!
