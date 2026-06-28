# Customer Accounts Microservice

[![Build Status](https://github.com/mdazharulislamnk/devops_capstone_project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/mdazharulislamnk/devops_capstone_project/actions/workflows/ci-build.yaml)

## Project Overview
This repository contains the final Capstone Project for the DevOps and Software Engineering Professional Certificate. It implements a RESTful microservice for managing Customer Accounts, built using Python and the Flask framework.

The project demonstrates proficiency in the following DevOps and software engineering practices:
- **Agile Development:** Organizing work using Kanban boards, Sprints, and User Stories.
- **RESTful APIs:** Implementing Create, Read, Update, Delete, and List (CRUDL) operations.
- **Test-Driven Development (TDD):** Writing automated unit tests using `nose` and achieving code coverage.
- **Continuous Integration (CI):** Automating linting (Flake8, Pylint) and testing using GitHub Actions.
- **Security:** Implementing CORS policies and Talisman security headers.
- **Containerization:** Packaging the microservice into a Docker image.
- **Continuous Deployment (CD) & Kubernetes:** Deploying the Docker image to a Kubernetes cluster and automating the pipeline using Tekton.

## Technology Stack
- **Language:** Python 3.9+
- **Framework:** Flask, Flask-RESTX
- **Database:** PostgreSQL / SQLite (via SQLAlchemy)
- **Testing:** `nosetests`, `coverage`
- **Linting:** `flake8`, `pylint`
- **CI/CD:** GitHub Actions, Tekton
- **Deployment:** Docker, Kubernetes

## API Endpoints
The microservice exposes the following RESTful API endpoints:
- `POST /accounts` - Create a new account
- `GET /accounts` - List all accounts
- `GET /accounts/{id}` - Read a specific account
- `PUT /accounts/{id}` - Update a specific account
- `DELETE /accounts/{id}` - Delete a specific account

## Local Development Setup

### Prerequisites
- Python 3.9 or higher
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mdazharulislamnk/devops_capstone_project.git
   cd devops_capstone_project
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests
To run unit tests and generate a coverage report:
```bash
nosetests
```

### Running the Application
To start the Flask development server:
```bash
flask run
```
The API will be available at `http://127.0.0.1:5000/`.

## License
This project is licensed under the MIT License.
