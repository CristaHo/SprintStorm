"""
Handles user database operations
"""
from sqlalchemy import text

from src.utils.database import db
from src.utils.logging import log


def delete_user_by_id(uid):
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
