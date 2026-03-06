graph TD
    %% Define styles
    classDef client fill:#f9f,stroke:#333,stroke-width:2px;
    classDef framework fill:#e1f5fe,stroke:#0277bd,stroke-width:2px;
    classDef middleware fill:#fff9c4,stroke:#fbc02d,stroke-width:1px,stroke-dasharray: 5 5;
    classDef logic fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef data fill:#ede7f6,stroke:#5e35b1,stroke-width:2px;
    classDef db fill:#fbe9e7,stroke:#bf360c,stroke-width:2px;

    %% Elements
    Client[Client<br/>(Postman / Frontend)]:::client

    subgraph Flask_Application [Flask Application (app.py)]
        direction TB
        ApiRoutes[API Routes / Endpoints<br/>(Blueprint Definition)]:::framework
        
        subgraph Middleware_Chain [Request Handling Chain]
            direction LR
            RateLimiter[Rate Limiter<br/>(Flask-Limiter)]:::middleware
            JwtAuth[JWT Auth Layer<br/>(Flask-JWT-Extended)]:::middleware
        end
    end

    ServiceLayer[Service Layer<br/>(services.py)<br/>Business Logic]:::logic
    DataModels[Database Models<br/>(models.py)<br/>SQLAlchemy ORM]:::data
    Database[(MySQL Database)]:::db

    %% Flow/Connections
    Client -->|HTTP Requests| ApiRoutes
    ApiRoutes --> RateLimiter
    RateLimiter --> JwtAuth
    JwtAuth -->|Valid Request| ServiceLayer
    ServiceLayer -->|Data Operations| DataModels
    DataModels -->|SQL Queries| Database
    Database -->|Data Result| DataModels
    DataModels -->|Python Objects| ServiceLayer
    ServiceLayer -->|Response Data| ApiRoutes
    ApiRoutes -->|HTTP Response| Client

    %% Legend/Notes
    linkStyle 0,1,2,3,4,5,6,7,8,9 stroke:#333,stroke-width:1px;
