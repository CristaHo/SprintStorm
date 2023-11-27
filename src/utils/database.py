"""
    This module is used to connect to the database.
"""
from flask_sqlalchemy import SQLAlchemy
from utils import config
from src.app import app

app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url()
db = SQLAlchemy(app)
