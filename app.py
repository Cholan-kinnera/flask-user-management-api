from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from extensions import db
from models import User
import services

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost/flask_user_id"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)
db.init_app(app)

with app.app_context():
    db.create_all()


    #health checkpoint
@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})  

            
            #login jwt
@app.route("/login", methods=["POST"])                     
def login():
    data = request.get_json()
    user = services.get_user_by_email(data["email"])

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity=str(user.id))
    return jsonify({
        "access_token": token
    })



                #limiter....
@app.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 5, type=int)
    if page < 1 or limit < 1:
        return jsonify({"error": "Invalid pagination values"}), 400
    users = services.get_all_users(page, limit)
    return jsonify({
        "page": page,
        "limit": limit,
        "users": [user.to_dict() for user in users]
    })

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = services.get_user(user_id)

    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()


      #input validation...
    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400
    if not data.get("email"):
        return jsonify({"error": "Email is required"}), 400
    user = services.create_user(
        data["name"],
        data["email"]
    )
    return jsonify(user.to_dict()), 201



@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    user = services.update_user(
        user_id,
        data["name"],
        data["email"]
    )

    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())



@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    success = services.delete_user(user_id)

    if not success:
        return jsonify({"error": "User not found"}), 404 
    return jsonify({"message": "User deleted"})


if __name__ == "__main__":
    app.run(debug=True)