from flask import Flask, request, render_template
from utils.reference_handler import create_reference

from app import app

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