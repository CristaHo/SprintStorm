
from flask_sqlalchemy import SQLAlchemy
from utils.environment import read_postgres_url
from src.app import app

sql_url = read_postgres_url()
if sql_url is None:
    raise RuntimeError("No SQL URL was found. Connection cannot be made.")

app.config["SQLALCHEMY_DATABASE_URI"] = sql_url
DB = SQLAlchemy(app)