"""
Handles book database operations
"""
from sqlalchemy import text
from src.utils.database import db

def get_all():
    """
    Gets all books from database
    """
    sql = text("SELECT * FROM book")

    result = db.session.execute(sql)

    return result.fetchall()

def insert_one(ref):
    """
    Inserts one book into database
    """
    sql = text("INSERT INTO book (author, title, year, publisher)"
            " VALUES (:author, :title, :year, :publisher)")
    db.session.execute(sql, {"author":ref["author"], "title":ref["title"],
                             "year":ref["year"], "publisher":ref["publisher"]})
    db.session.commit()
