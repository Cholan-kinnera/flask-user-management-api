from models import User
from werkzeug.security import generate_password_hash
from extensions import db


def get_all_users(page, limit):
    users = User.query.paginate(page=page, per_page=limit)
    return users.items


def get_user(user_id):
    return User.query.get(user_id)


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

## Using hashed_password 

def create_user(name, email,password):
    hashed_password = generate_password_hash(password)
    new_user = User(
        name=name, 
        email=email,
        password=hashed_password
        )
    
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id,name,email):
    user = User.query.get(user_id)
    if not user:
        return None
    user.name = name
    user.email = email
    db.session.commit()
    return user

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True



  
