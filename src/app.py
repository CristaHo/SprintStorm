"""
Defines the Flask applications dependencies and database connection.
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.environ.get('ENVIRONMENT') == 'production':
    sql_url = os.environ.get('POSTGRES_URL') or None
else:
    sql_url = os.environ.get('TEST_POSTGRES_URL') or None
if sql_url is None:
    raise RuntimeError("No SQL URL was found. Connection cannot be made.")

app = Flask(__name__)
app.config["DATABASE_URI"] = sql_url
db = SQLAlchemy(app)

@app.route("/test")
def hello_world():
    """
    A basic endpoint to test the app
    """

    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
