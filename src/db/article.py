"""
Handles article databse
"""

from sqlalchemy import text
from src.utils.database import db

def get_all():
    """Gets all articles from database"""
    sql = text("SELECT * FROM article")

    result = db.session.execute(sql)

    return result.fetchall()

def insert_one(ref):
    """Inserts one article into database"""
    sql = text("INSERT INTO article (author, title, year, journal, volume, pages)"
            " VALUES (:author, :title, :year, :journal, :volume, :pages)")
    db.session.execute(sql, {"author":ref["author"],
                             "title":ref["title"], "year":ref["year"],
                             "journal":ref["journal"], "volume":ref["volume"],
                             "pages":ref["pages"]})
    db.session.commit()
