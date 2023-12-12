"""
Handles user database operations
"""
from sqlalchemy import text

from src.utils.database import db
from src.utils.logging import log


def delete_user(uid):
    """
    Deletes a user from the database
    """
    sql = text("DELETE FROM users WHERE id =:uid")

    result = db.session.execute(sql,{"uid":uid})
    affected_rows = result.rowcount

    if affected_rows > 0:
        log.info(f"User with id {uid} deleted successfully.")
    else:
        log.warning(f"No user with id {uid} found for deletion.")

def get_user_id_by_username(username):
    """
    Returns a user id for the given username
    """
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username}).fetchone()

    if result:
        user_id = result[0]
        log.info(f"User ID for username {username}: {user_id}")
        return user_id

    log.warning(f"No user found for username: {username}")
    return None
