from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from extensions import db
import services
from dotenv import load_dotenv
import os
import re
import logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt='%Y-%m-%dT%H:%M:%S%z')

app = Flask(__name__)

app.json.sort_keys = False


limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

limiter.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)

db.init_app(app)

with app.app_context():
    db.create_all()


# Health check
@app.route("/")
def hello():
    return jsonify({"message": "Flask User API Running"})


# Register User
@app.route("/api/v1/register", methods=["POST"])
@limiter.limit("5 per minute")
def register():


    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body required"}), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    logging.info(f"Register request for email: {email}")

    if not name:
        return jsonify({"error": "Name is required"}), 400
    
     #EMAIL VALIDATION
    email_pattern = r"[^@]+@[^@]+\.[^@]+"                
    if not re.match(email_pattern, email):
        return jsonify({"error": "Email is required"}), 400
    if not password:
        return jsonify({"error": "Password is required"}), 400

    # Check duplicate email
    existing_user = services.get_user_by_email(email)
    if existing_user:
        return jsonify({"error": "Email already registered"}), 409
    new_user = services.create_user(name, email, password)
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400
    return jsonify(new_user.to_dict()), 201


# Login
@app.route("/api/v1/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():

    data = request.get_json()
    logging.info(f"Login request for email: {data.get('email')}")

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400

    user = services.get_user_by_email(data["email"])

    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))

    return jsonify({"access_token": token})



# Get All Users (Protected)
@app.route("/api/v1/users", methods=["GET"])
@jwt_required()
def get_users():

    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 5, type=int)

    if page < 1 or limit < 1:
        return jsonify({"error": "Invalid pagination values"}), 400

    if limit > 50:
        limit = 50

    users = services.get_all_users(page, limit)

    return jsonify({
        "page": page,
        "limit": limit,
        "users": [user.to_dict() for user in users]
    })


@app.route("/api/v1/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    user = services.get_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict())


# Get User by ID
@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):

    user = services.get_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict())



# Update User
@app.route("/api/v1/users/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body required"}), 400

    user = services.update_user(
        user_id,
        data.get("name"),
        data.get("email")
    )

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict())


# Delete User
@app.route("/api/v1/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):

    success = services.delete_user(user_id)

    if not success:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted"})

#ERROR HANDLING

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)