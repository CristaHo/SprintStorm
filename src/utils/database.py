"""
    This module is used to connect to the database.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from src.utils import config
from src.app import app
from src.utils.logging import log

app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url()
db = SQLAlchemy(app)

def init_tables(schema_path: str="sql/schema.sql"):
    """
    Reads the schema.sql file (by default sql/schema.sql) 
    which initializes all tables"""
    log.info("Creating schema for database...")
    with open(schema_path, encoding="utf-8") as file:
        sql = text(file.read())
        db.session.execute(sql)
        db.session.commit()

def drop_tables(drop_tables_path: str="sql/drop_tables.sql"):
    """
    Reads drop_tables.sql file (by default sql/drop_tables.sql) 
    and drops all tables used.

    TODO: When users are saved into the database, make sure the user's deletion
    CASCADES the references owned by user.
    """
    log.info("Dropping all tables...")
    with open(drop_tables_path, encoding="utf-8") as file:
        sql = text(file.read())
        db.session.execute(sql)
        db.session.commit()

def reset_database():
    """
    Runs drop_tables() and init_database(). 
    Database should be left empty with tables
    """
    log.info("Resetting database...")
    drop_tables()
    init_tables()
