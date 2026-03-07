# Flask User Management API

A production-ready RESTful backend API built with **Flask** and **MySQL**. This project demonstrates high-level backend engineering practices including secure JWT authentication, modular architecture, and API security.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/flask-latest-green.svg)
![MySQL](https://img.shields.io/badge/mysql-latest-orange.svg)

---

## 🏗️ System Architecture

The following diagram illustrates the request flow, showing how the application separates concerns into security middleware, business logic, and database operations.

```mermaid
graph LR
    %% Styles
    classDef client fill:#f5f5f5,stroke:#333;
    classDef flask fill:#e1f5fe,stroke:#0277bd;
    classDef logic fill:#e8f5e9,stroke:#2e7d32;
    classDef db fill:#fbe9e7,stroke:#bf360c;

    %% Nodes
    Client["Client (Postman/Frontend)"]:::client
    
    subgraph App ["Flask API (app.py)"]
        Routes["API Routes"]:::flask
        Auth["JWT & Rate Limiting"]:::flask
    end
    
    Service["Service Layer (services.py)"]:::logic
    Models["SQLAlchemy Models"]:::logic
    DB[("MySQL Database")]:::db

    %% Flow
    Client --> Routes
    Routes --> Auth
    Auth --> Service
    Service --> Models
    Models --> DB
