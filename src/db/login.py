"""Handles searching user from database
"""
from werkzeug.security import check_password_hash
from sqlalchemy import text
from flask import session
from src.utils.database import db
from src.utils.logging import log


def get_user(username: str):
    """Searches for added user by username

    :param username: username of wanted user
    :returns: user or none of no user was found
    """
    sql = text("SELECT id, password, username FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username}).fetchone()
    if result:
        return result
    return None

def check_user(username: str, password: str) -> bool:
    """
    Checks if the user given in the params can log in.

    The database is queried for an user with the username given.
    If user exists, the password is checked.
    If the given password and the password_hash gotten from the db
    match, save the user_id to local session.

    :param username: username of the user logging in
    :param password: plaintext password of the user logging in
    :returns: boolean, if the login was successful
    """
    log.info(f"Logging in as user {username}")
    user = get_user(username)

    if not user:
        log.error(f"User {username} does not exist")
        return False

    password_hash = user[1]
    if check_password_hash(password_hash, password):
        session["uid"] = user.id
        return True
    return False
