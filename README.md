# FastAPI Task Management System

A lightweight **task management API** built with **FastAPI**, supporting task creation, retrieval, updating, and deletion. Features include **JSON file-based storage**, **versioned backups**, and a clean, maintainable project architecture.

---

## Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Usage](#usage)
* [API Endpoints](#api-endpoints)
* [Configuration](#configuration)
* [Backups](#backups)
* [Contributing](#contributing)
* [License](#license)

---

## Features

* **CRUD operations** for tasks
* **File-based storage** using JSON arrays
* **Atomic writes** to prevent data corruption
* **Timestamped, human-readable backups**
* **Absolute path configuration** for robust file handling
* Lightweight, dependency-minimized architecture

---

## Project Structure

```text
fastapi-task-management-system/
│
├── app/
│   ├── main.py                  # FastAPI application entry point
│   ├── core/
│   │   └── config.py            # Application configuration (paths, env)
│   ├── routers/                 # API route definitions
│   ├── schemas/                 # Pydantic models for validation
│   ├── services/                # Business logic and task management
│   └── data/
│       ├── tasks.json           # Primary task storage
│       └── backups/             # Timestamped backup files
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/fastapi-task-management-system.git
cd fastapi-task-management-system
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

* API will run at: `http://127.0.0.1:8000`
* Swagger UI documentation: `http://127.0.0.1:8000/docs`
* ReDoc documentation: `http://127.0.0.1:8000/redoc`

---

## API Endpoints

| Method | Endpoint      | Description                     |
| ------ | ------------- | ------------------------------- |
| GET    | `/tasks/`     | Get all tasks                   |
| POST   | `/tasks/`     | Create a new task               |
| PUT    | `/tasks/{id}` | Update an existing task         |
| DELETE | `/tasks/{id}` | Delete a task                   |
| GET    | `/export/`    | Export tasks as JSON (download) |

---

## Configuration

All configuration is in `app/core/config.py`:

* `TASKS_FILE` → Path to the JSON file storing tasks
* `BACKUP_DIR` → Directory for timestamped backups
* `BACKEND_CORS_ORIGINS` → List of allowed CORS origins

Paths use **absolute Path objects**, so file access works regardless of working directory.

---

## Backups

* Backups are stored in **`app/data/backups/`**
* Backup filenames are **human-readable and timestamped**:

```
tasks_backup_YYYY-MM-DD_HH-MM-SS.json
```

* Ensures no overwriting of multiple backups created at the same time

Example:

```
tasks_backup_2026-02-28_10-15-30.json
tasks_backup_2026-02-28_10-45-12.json
```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "feat: add my feature"`
4. Push to branch: `git push origin feature/my-feature`
5. Open a pull request

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

