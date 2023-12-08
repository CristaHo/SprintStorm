"""
Handles article databse
"""

from sqlalchemy import text
from src.utils.database import db
from src.references.article import Article
from src.utils.logging import log

def get_all(uid) -> list[Article] | None:
    """Gets all articles from database"""
    sql = text("SELECT * FROM article WHERE user_id =:uid")

    result = db.session.execute(sql,{"uid":uid}).fetchall()
    if result:
        articles = []
        for item in result:
            articles.append(Article(parse_fetchall(item)))
        return articles

    log.info("No articles found from database.")
    return None



def insert_one(ref):
    """Inserts one article into database"""
    sql = text("INSERT INTO article"
               " (cite_key, author, title, year, journal, volume, pages, category_id,user_id)"
               " VALUES (:key, :author, :title, :year, :journal, :volume, :pages,"
                " :category_id,:user_id)")
    db.session.execute(sql, {"key": ref["key"], "author":ref["author"],
                             "title":ref["title"], "year":ref["year"],
                             "journal":ref["journal"], "volume":ref["volume"],
                             "pages":ref["pages"], "category_id":ref["category_id"],
                             "user_id":ref["user_id"]})
    db.session.commit()

def parse_fetchall(rows):
    """
    Parses article fetchall from get_all and fits the rows inside an object
    """
    # pylint: disable=duplicate-code
    fields = {
            "key": rows[1],
            "author": rows[2],
            "title": rows[3],
            "year": rows[4],
            "journal": rows[5],
            "volume": rows[6],
            "pages": rows[7],
            "category_id": rows[8]
            }

    return fields

def delete_one(uid, cite_key):
    """
    Deletes one article from database
    """
    sql = text("DELETE FROM article WHERE user_id =:uid AND cite_key =:cite_key")
    db.session.execute(sql,{"uid":uid, "cite_key":cite_key})
    db.session.commit()
