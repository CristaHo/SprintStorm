"""
Defines the Flask applications dependencies and database connection.
"""

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from utils.reference_handler import create_reference
from utils.environment import read_postgres_url

sql_url = read_postgres_url()
if sql_url is None:
    raise RuntimeError("No SQL URL was found. Connection cannot be made.")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = sql_url
db = SQLAlchemy(app)

app.register_blueprint(add_reference_bp)
app.register_blueprint(view_reference_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
