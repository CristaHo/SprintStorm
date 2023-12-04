"""
Handles book database operations
"""
from sqlalchemy import text

from src.utils.database import db
from src.references.book import Book

def get_all() -> list[Book] | None:
    """
    Gets all books from database
    """
    sql = text("SELECT * FROM book")

    result = db.session.execute(sql).fetchall()
    if result:
        books = []
        for item in result:
            books.append(Book(parse_fetchall(item)))
        return books

    return None

def insert_one(ref):
    """
    Inserts one book into database
    """
    sql = text("INSERT INTO book (cite_key, author, title, year, publisher, address)"
               " VALUES (:key, :author, :title, :year, :publisher, :address)")
    parsed_reference = {
        "key": ref["key"],
        "author": ref["author"],
        "title": ref["title"],
        "year": ref["year"],
        "publisher": ref["publisher"],
        "address": ref["address"]
    }
    db.session.execute(sql, parsed_reference)
    db.session.commit()

def parse_fetchall(rows):
    """
    Parses book fetchall from get_all and fits the rows inside an object
    """
    # pylint: disable=duplicate-code
    fields = {
            "key": rows[1],
            "author": rows[2],
            "title": rows[3],
            "year": rows[4],
            "publisher": rows[5],
            "address": rows[6],
            }

    return fields
