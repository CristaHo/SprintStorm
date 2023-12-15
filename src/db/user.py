"""
Handles user database operations
"""
from sqlalchemy import text, exc

from src.utils.database import db
from src.utils.logging import log

def delete_user_by_id(uid):
    """
    Deletes a user from the database
    """
    try:
        db.session.execute(text("DELETE FROM category WHERE user_id = :uid"), {"uid": uid})
        db.session.execute(text("DELETE FROM misc WHERE user_id = :uid"), {"uid": uid})
        db.session.execute(text("DELETE FROM book WHERE user_id = :uid"), {"uid": uid})
        db.session.execute(text("DELETE FROM article WHERE user_id = :uid"), {"uid": uid})
        db.session.execute(text("DELETE FROM users WHERE id = :uid"), {"uid": uid})
        
        db.session.commit()
        log.info(f"User with id {uid} deleted successfully.")

    except exc.SQLAlchemyError as e:
        db.session.rollback()
        log.error(f"Error deleting user with id {uid}: {str(e)}")
