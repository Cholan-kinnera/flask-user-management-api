# Flask User Management API

A production-ready RESTful backend API built with **Flask** and **MySQL**. This project demonstrates high-level backend engineering practices including secure JWT authentication, modular architecture, and API security.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/flask-latest-green.svg)
![MySQL](https://img.shields.io/badge/mysql-latest-orange.svg)

---

## 🏗️ System Architecture

## Backend Architecture Overview

The system follows a layered architecture separating request handling, security middleware, business logic, and data access. This improves maintainability, scalability, and overall system design.

The backend is designed using a layered architecture to ensure clear separation of concerns between request handling, security middleware, business logic, and database access.


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
