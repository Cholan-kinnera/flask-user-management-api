from models import User
from extensions import db


def get_all_users(page, limit):
    users = User.query.paginate(page=page, per_page=limit)
    return users.items


def get_user(user_id):
    return User.query.get(user_id)



def create_user(name, email):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id,name,email):
    user = User.query.get(user_id)
    user.name = name
    user.email = email
    db.session.commit()
    return user

def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return user


def get_user_by_email(email):
    user =  User.query.filter_by(email=email).first()
    return user
  
