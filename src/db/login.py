"""Handles searching user from database
"""
from werkzeug.security import check_password_hash
from sqlalchemy import text
from flask import session
from src.utils.database import db

def get_user(username, password):
    """Searches for added user"""
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False

    hash_value = user.password
    if check_password_hash(hash_value, password):
        session["uid"] = user.id
        return True
    return False
