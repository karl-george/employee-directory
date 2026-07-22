# Employee Directory

[![Application CI](https://github.com/karl-george/employee-directory/actions/workflows/ci.yml/badge.svg)](https://github.com/karl-george/employee-directory/actions/workflows/ci.yml)

A simple employee directory web application built with **Python**, **Flask**, and **SQLite**.

The application was developed as part of a DevOps learning project and is used throughout a homelab to demonstrate modern deployment practices including Docker, GitHub Container Registry (GHCR), Kubernetes, and Infrastructure as Code.

---

## Features

- View all employees
- Add new employees
- Edit existing employees
- Delete employees
- SQLite database backend
- Responsive web interface
- Production-ready Gunicorn configuration
- Docker support
- Automated testing with Pytest

---

## Technology Stack

| Component          | Technology                |
| ------------------ | ------------------------- |
| Language           | Python 3                  |
| Framework          | Flask                     |
| Database           | SQLite                    |
| WSGI Server        | Gunicorn                  |
| Testing            | Pytest                    |
| Containerisation   | Docker                    |
| Container Registry | GitHub Container Registry |
| Orchestration      | Kubernetes                |

---

## Project Structure

```
employee-directory/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/
│   ├── static/
│   └── ...
├── tests/
├── Dockerfile
├── .dockerignore
└── README.md
```

---

## Running Locally

Clone the repository.

```bash
git clone https://github.com/<your-username>/employee-directory.git
cd employee-directory
```

Create a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies.

```bash
pip install -r app/requirements.txt
```

Start the application.

```bash
cd app

gunicorn \
    --workers 3 \
    --bind 0.0.0.0:8000 \
    app:app
```

The application will be available at:

```
http://localhost:8000
```

---

## Running the Test Suite

Run all unit tests using Pytest.

```bash
python -m pytest -v
```

---

# Docker

Build the container image.

```bash
docker build \
    -t ghcr.io/<github-username>/employee-directory:v1.0.0 \
    .
```

Run the container.

```bash
docker run \
    --rm \
    -p 8000:8000 \
    ghcr.io/<github-username>/employee-directory:v1.0.0
```

The application will be available at:

```
http://localhost:8000
```

---

## Kubernetes Deployment

The Kubernetes manifests for deploying this application are maintained separately in the **homelab-infrastructure** repository.

That repository contains:

- Namespace
- Deployment
- Service
- Future Ingress configuration
- Infrastructure automation

---

## Development Workflow

1. Implement a feature.
2. Run the test suite.
3. Commit and push changes.
4. Build a new Docker image.
5. Publish the image to GitHub Container Registry.
6. Update the Kubernetes Deployment to use the new image version.

---
