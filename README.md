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
    classDef client fill:#f5f5f5,stroke:#333,stroke-width:2px;
    classDef flask fill:#e1f5fe,stroke:#0277bd,stroke-width:2px;
    classDef logic fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef data fill:#ede7f6,stroke:#5e35b1,stroke-width:2px;
    classDef db fill:#fbe9e7,stroke:#bf360c,stroke-width:2px;

    %% Client Layer
    Client["Client<br/>(Postman / Frontend)"]:::client

    %% Backend Layer
    subgraph Backend ["Backend Layer"]
        Flask["Flask API<br/>(app.py)"]:::flask
        Auth["Auth & Rate Limiting"]:::flask
    end

    %% Business Logic Layer
    Service["Service Layer<br/>(services.py)"]:::logic

    %% Data Layer
    subgraph Data ["Data Layer"]
        Models["SQLAlchemy Models<br/>(models.py)"]:::data
        Database[("MySQL<br/>Database")]:::db
    end

    %% Flow
    Client --> Flask
    Flask --> Auth
    Auth --> Service
    Service --> Models
    Models --> Database
