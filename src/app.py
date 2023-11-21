"""
Defines the Flask applications dependencies and database connection.
"""
import os
from flask import Flask, request, render_template
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

@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    """
    Route for handling adding a new reference
    """
    if request.method == "GET":
        return render_template("add_reference.html")

    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']

        return f"{author}<br>{title}<br>{year}"
        # Add processing for reference information

    return None


if __name__ == "__main__":
    app.run(host='0.0.0.0')
