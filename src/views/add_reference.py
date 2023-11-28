"""
Blueprint for handling the addition of new references.
"""

from flask import Blueprint, request, render_template
from src.utils.reference_handler import reference_handler

add_reference_bp = Blueprint('add_reference', __name__)
choose_reference_bp = Blueprint('choose-reference', __name__)

@choose_reference_bp.route("/choose_reference", methods=["GET", "POST"])
def choose_reference():
    if request.method == "GET":
        return render_template("add_reference.html")
    if request.method == "POST":
        choice = request.args["ref"]

        return render_template("add_reference.html", choice)


@add_reference_bp.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    """
    Route for handling adding a new reference.
    """
    if request.method == "GET":
        return render_template("add_reference.html")

    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']

        ref = reference_handler.create_reference(
            reftype='ref',
            fields={'author':author, 'title':title, 'year':year})

        return f"{ref.author}<br>{ref.title}<br>{ref.year}"

        # Add processing for reference into database

    return None
