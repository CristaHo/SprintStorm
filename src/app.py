"""
Defines the Flask applications dependencies and database connection.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views.add_reference import add_reference_bp
from views.view_reference import view_reference_bp
from utils.environment import read_postgres_url

sql_url = read_postgres_url()
if sql_url is None:
    raise RuntimeError("No SQL URL was found. Connection cannot be made.")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = sql_url
db = SQLAlchemy(app)


app.register_blueprint(add_reference_bp)
app.register_blueprint(view_reference_bp)

@app.route("/test")
def hello_world():
    """
    A basic endpoint to test the app
    """

    return "<p>Hello, World!</p>"

@app.route("/")
def index():
    """
    Route for viewing index-page
    """
    return render_template("index.html")

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

        ref = create_reference(author, title, year)

        return f"{ref.author}<br>{ref.title}<br>{ref.year}"

        # Add processing for reference into database

    return None

@app.route("/view_reference")
def view_reference():
    """
    Route for viewing added references
    """
    reference_list = [] #Add way to get references

    return render_template("view_reference.html", references=reference_list)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
