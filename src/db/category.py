"""
Handles category database operations
"""
from sqlalchemy import text

from src.utils.database import db
from src.utils.logging import log

def get_all(user_id):
    """
    Gets all categories for a user
    """
    sql = text("SELECT * FROM category WHERE user_id=:user_id")

    results = db.session.execute(sql, {"user_id":user_id})
    if results:
        return results

    log.info("No categories found")
    return None

def insert_one(fields):
    """
    Inserts one category into database
    """
    sql = text("INSERT INTO category (name, user_id)"
               " VALUES (:name, :user_id)")

    db.session.execute(sql, fields)
    db.session.commit()

def delete_one(field):
    """
    Deletes one category from database
    """
    sql = text("DELETE FROM category WHERE id=:id")

    db.session.execute(sql, field)
    db.session.commit()
