# Flask User Management API

A **production-style RESTful backend API** built with **Flask and MySQL**.  
This project demonstrates real-world backend engineering practices including **JWT authentication, modular architecture, secure password hashing, rate limiting, and database-driven APIs**.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Flask](https://img.shields.io/badge/flask-latest-green)
![MySQL](https://img.shields.io/badge/mysql-latest-orange)
![JWT](https://img.shields.io/badge/auth-JWT-yellow)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)

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
│
├── app.py            # Flask application and API routes
├── models.py         # SQLAlchemy database models
├── services.py       # Business logic layer
├── extensions.py     # Flask extensions initialization
├── requirements.txt  # Python dependencies
├── .env.example      # Example environment variables
├── .gitignore        # Git ignored files
└── README.md         # Project documentation
```



### Explanation

| File | Purpose |
|-----|--------|
| `app.py` | Main Flask application and API routes |
| `models.py` | SQLAlchemy database models |
| `services.py` | Business logic and database operations |
| `extensions.py` | Shared Flask extensions |
| `requirements.txt` | Project dependencies |
| `.env.example` | Example environment configuration |

---

# System Architecture

## Backend Architecture Overview

The backend is designed using a **layered architecture** to ensure clear separation of concerns between request handling, security middleware, business logic, and database access.

This design improves:

- maintainability
- scalability
- readability of the codebase
- modular development

```mermaid
flowchart LR

%% Nodes
A[Client<br>Postman / Frontend]

B[Flask API<br>app.py]

C[JWT Authentication]

D[Rate Limiting]

E[Service Layer<br>services.py]

F[SQLAlchemy Models<br>models.py]

G[(MySQL Database)]

%% Flow
A --> B
B --> C
B --> D
C --> E
D --> E
E --> F
F --> G

%% Styling
classDef client fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px,color:#000
classDef api fill:#E8F5E9,stroke:#43A047,stroke-width:2px,color:#000
classDef security fill:#FFF8E1,stroke:#FB8C00,stroke-width:2px,color:#000
classDef service fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px,color:#000
classDef data fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#000
classDef database fill:#FCE4EC,stroke:#D81B60,stroke-width:2px,color:#000

class A client
class B api
class C,D security
class E service
class F data
class G database
```
