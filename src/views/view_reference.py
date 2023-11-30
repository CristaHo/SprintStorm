"""
Blueprint for handling viewing references.
"""

from flask import render_template
from src.app import app
from src.db.reference import get_all

@app.route("/view_reference")
def view_reference():
    """
    Route for viewing added references.
    """
    reference_list = get_all()

    return render_template("view_reference.html", references=reference_list)
