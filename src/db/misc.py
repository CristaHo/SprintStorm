"""
Handle misc database operations
"""
from sqlalchemy import text

from src.utils.database import db
from src.references.misc import Misc
from src.utils.logging import log

def get_all(uid) -> list[Misc] | None:
    """
    Gets all misc from database
    """

    sql = text("SELECT * FROM misc WHERE user_id =:uid")

    result = db.session.execute(sql, {"uid": uid}).fetchall()

    if result:
        miscs = []
        for item in result:
            miscs.append(Misc(parse_fetchall(item)))
        return miscs

    log.info("No miscs found from database")
    return None

def insert_one(ref):
    """
    Inserts one misc into database
    """
    sql = text("INSERT INTO misc (cite_key, author,"
               " title, year, url, urldate, category_id, user_id)"
               " VALUES (:key, :author,:title, :year, :url, :urldate, :category_id, :user_id)")
    # pylint: disable=duplicate-code
    parsed_reference = {
        "key": ref["key"],
        "author": ref["author"],
        "title": ref["title"],
        "year": ref["year"],
        "url": ref["url"],
        "urldate": ref["urldate"],
        "category_id": ref["category_id"],
        "user_id": ref["user_id"]
    }
    db.session.execute(sql, parsed_reference)
    db.session.commit()

def delete_one(uid, cite_key):
    """
    Deletes one misc from database
    """
    sql = text("DELETE FROM misc WHERE user_id =:uid AND cite_key =:cite_key")
    db.session.execute(sql,{"uid":uid, "cite_key":cite_key})
    db.session.commit()

def parse_fetchall(rows):
    """
    Parses misc fetchall from get_all and fits the rows inside an object
    """
    # pylint: disable=duplicate-code
    fields = {
            "key": rows[1],
            "author": rows[2],
            "title": rows[3],
            "year": rows[4],
            "url": rows[5],
            "urldate": rows[6],
            "category_id": rows[7]
            }

    return fields
