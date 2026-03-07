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

## Request Flow
This diagram shows how an API request flows through the backend system from the client to the database and back to the client.
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

## Installation

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Cholan-kinnera/flask-user-management-api.git
```

Navigate into the project directory:

```bash
cd flask-user-management-api
```

---

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory.

Example configuration:

```env
DATABASE_URL=mysql+pymysql://root:password@localhost/flask_user_db
JWT_SECRET_KEY=your_secret_key
```

A template is provided in:

```
.env.example
```

---

### 5. Run the Application

Start the Flask server:

```bash
python app.py
```

The API will start running at:

```
http://localhost:5000
```
## Verify the Server

You can test the API using Postman or curl.

Example:

```bash
curl http://localhost:5000
```

## Environment Variables

The application uses environment variables for configuration.  
Create a `.env` file in the root directory of the project.

An example configuration is provided in:

```
.env.example
```

Copy the example file and update it with your own values.

### Example `.env` configuration

```
DATABASE_URL=mysql+pymysql://root:password@localhost/flask_user_db
JWT_SECRET_KEY=your_secret_key
```

### Explanation

| Variable | Description |
|--------|-------------|
| DATABASE_URL | Connection string used to connect to the MySQL database |
| JWT_SECRET_KEY | Secret key used to sign and verify JWT authentication tokens |

### Creating the `.env` file

You can create the `.env` file manually or run:

```bash
cp .env.example .env
```

Then edit the file and add your configuration values.

### Important

The `.env` file is ignored by Git to prevent sensitive credentials from being committed to the repository.  
Only `.env.example` is included to show the required environment variables.

Make sure the `.env` file exists before running the application.


## API Documentation

### Base URL

```
http://localhost:5000
```

All protected endpoints require the following header:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## Register User

Creates a new user account.

### Endpoint

```
POST /api/v1/register
```

### Request Body

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

### Success Response

```json
Status: 201 Created

{
  "message": "User registered successfully"
}
```

### Error Response

```json
Status: 409 Conflict

{
  "error": "Email already exists"
}
```

---

## Login

Authenticates a user and returns a JWT access token.

### Endpoint

```
POST /api/v1/login
```

### Request Body

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

### Success Response

```json
Status: 200 OK

{
  "access_token": "your_jwt_token"
}
```

---

## Get Users

Returns a list of users with pagination support.

### Endpoint

```
GET /api/v1/users
```

### Query Parameters

```
?page=1
?limit=10
```

### Headers

```
Authorization: Bearer <JWT_TOKEN>
```

### Example Response

```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "created_at": "2026-03-06"
    }
  ]
}
```

---

## Get Single User

Returns details of a specific user.

### Endpoint

```
GET /api/v1/users/<id>
```

### Headers

```
Authorization: Bearer <JWT_TOKEN>
```

---

## Update User

Updates an existing user's information.

### Endpoint

```
PUT /api/v1/users/<id>
```

### Headers

```
Authorization: Bearer <JWT_TOKEN>
```

### Request Body

```json
{
  "name": "Updated Name",
  "email": "updated@email.com"
}
```

---

## Delete User

Deletes a user from the system.

### Endpoint

```
DELETE /api/v1/users/<id>
```

### Headers

```
Authorization: Bearer <JWT_TOKEN>
```
## API Testing

All API endpoints were tested using **Postman** to ensure correct functionality, authentication handling, and proper response formatting.

The following scenarios were tested:

- User registration
- User login and JWT token generation
- Accessing protected routes using JWT authentication
- Retrieving users with pagination
- Updating user information
- Deleting users from the database

Each request was validated for:

- Correct HTTP status codes
- Proper JSON responses
- Authentication and authorization checks
- Input validation and error handling

➡️ [View Postman Testing Screenshots](#screenshots)


