# Flask User Management API

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&color=F7DF1E&center=true&vCenter=true&width=700&lines=Flask+User+Management+API;JWT+Authentication+Backend;Production+Style+REST+API;Python+Flask+MySQL+Architecture" />
</p>

A **production-style RESTful backend API** built using **Flask and MySQL**.

This project demonstrates real backend engineering practices such as:

- JWT authentication
- modular service architecture
- password hashing
- rate limiting
- database-driven APIs

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Flask](https://img.shields.io/badge/flask-latest-green)
![MySQL](https://img.shields.io/badge/mysql-database-orange)
![JWT](https://img.shields.io/badge/authentication-JWT-yellow)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)

---

# Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [System Architecture](#system-architecture)
- [Request Flow](#request-flow)
- [System Design Overview](#system-design-overview)
- [Installation](#installation)
- [Verify the Server](#verify-the-server)
- [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [API Testing](#api-testing)
- [Postman Testing Screenshots](#postman-testing-screenshots)

---

# Features

- User registration
- JWT authentication
- Password hashing
- CRUD user management
- Rate limiting for security
- Pagination support
- Modular backend architecture
- Environment variable configuration
- Structured logging

---

# Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | Flask |
| Language | Python |
| Database | MySQL |
| ORM | SQLAlchemy |
| Authentication | Flask-JWT-Extended |
| Security | Werkzeug |
| Rate Limiting | Flask-Limiter |
| Environment Config | python-dotenv |
| API Testing | Postman |
| Version Control | Git & GitHub |

---

# Project Structure

```
flask_user_manager/

├── app.py
├── models.py
├── services.py
├── extensions.py
├── requirements.txt
├── .env.example
├── .gitignore
├── screenshots/
└── README.md
```

| File | Purpose |
|-----|--------|
| app.py | Main Flask application |
| models.py | Database models |
| services.py | Business logic |
| extensions.py | Flask extensions |
| requirements.txt | Python dependencies |

---

# System Architecture

### Backend Architecture Overview

```mermaid
flowchart LR

A[Client<br/>Postman / Frontend]
B[Flask API<br/>app.py]
C[JWT Authentication]
D[Rate Limiting]
E[Service Layer<br/>services.py]
F[SQLAlchemy Models<br/>models.py]
G[(MySQL Database)]

A --> B
B --> C
B --> D
C --> E
D --> E
E --> F
F --> G
```

---

# Request Flow

```mermaid
sequenceDiagram

participant Client
participant FlaskAPI
participant ServiceLayer
participant Database

Client->>FlaskAPI: HTTP Request

Note over FlaskAPI: JWT Authentication
FlaskAPI->>FlaskAPI: Validate Token

Note over FlaskAPI: Rate Limiting
FlaskAPI->>FlaskAPI: Check Request Limits

FlaskAPI->>ServiceLayer: Process Business Logic
ServiceLayer->>Database: Query / Update Data
Database-->>ServiceLayer: Return Result
ServiceLayer-->>FlaskAPI: Response Data
FlaskAPI-->>Client: JSON Response
```

---

# System Design Overview

```mermaid
flowchart TB

subgraph Client
A[Postman / Frontend]
end

subgraph Backend API
B[Flask REST API]
end

subgraph Middleware
C[JWT Authentication]
D[Rate Limiting]
end

subgraph Application Layer
E[Service Layer]
end

subgraph Data Layer
F[SQLAlchemy ORM]
G[(MySQL Database)]
end

A --> B
B --> C
B --> D
C --> E
D --> E
E --> F
F --> G
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Cholan-kinnera/flask-user-management-api.git
cd flask-user-management-api
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```
.venv\Scripts\activate
```

macOS / Linux

```
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run server

```
python app.py
```

Server runs at

```
http://localhost:5000
```

---

# Verify the Server

Test API quickly:

```
curl http://localhost:5000
```

Or use **Postman**.

---

# Environment Variables

Create `.env` file

```
DATABASE_URL=mysql+pymysql://root:password@localhost/flask_user_db
JWT_SECRET_KEY=your_secret_key
```

Example available in

```
.env.example
```

---

# API Documentation

Base URL

```
http://localhost:5000
```

Protected routes require

```
Authorization: Bearer <JWT_TOKEN>
```

### Register User

```
POST /api/v1/register
```

### Login

```
POST /api/v1/login
```

### Get Users

```
GET /api/v1/users
```

### Update User

```
PUT /api/v1/users/<id>
```

### Delete User

```
DELETE /api/v1/users/<id>
```

---

# API Testing

All endpoints were tested using **Postman**.

Tested scenarios include:

- user registration
- login and JWT token generation
- accessing protected routes
- pagination
- update and delete operations

---

# Postman Testing Screenshots

Preview of API testing:

<p align="center">
<img src="screenshots/2.User-Register.png" width="45%">
<img src="screenshots/3.User-Login(JWT-Tokens).png" width="45%">
</p>

<p align="center">
<em>Postman testing of registration and login endpoints</em>
</p>

Full screenshots available here:

📸 **[Open Screenshots Folder](https://github.com/Cholan-kinnera/flask-user-management-api/tree/main/screenshots)**