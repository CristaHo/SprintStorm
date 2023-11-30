"""
Handles article databse
"""

from sqlalchemy import text
from src.utils.database import db
from src.references.article import Article

def get_all():
    """Gets all articles from database"""
    sql = text("SELECT * FROM article")

    result = db.session.execute(sql).fetchall()
    if result:
        articles = []
        for item in result:
            articles.append(Article(parse_fetchall(item)))
        return articles

    return None



def insert_one(ref):
    """Inserts one article into database"""
    sql = text("INSERT INTO article (author, title, year, journal, volume, pages)"
            " VALUES (:author, :title, :year, :journal, :volume, :pages)")
    db.session.execute(sql, {"author":ref["author"],
                             "title":ref["title"], "year":ref["year"],
                             "journal":ref["journal"], "volume":ref["volume"],
                             "pages":ref["pages"]})
    db.session.commit()

def parse_fetchall(rows):
    fields = {
            "key": rows[1],
            "author": rows[2],
            "title": rows[3],
            "year": rows[4],
            "journal": rows[5],
            "volume": rows[6],
            "pages": rows[7]
            }

    return fields
