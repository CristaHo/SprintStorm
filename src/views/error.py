"""
blueprint for handling error route
"""

from flask import render_template
from src.app import app

@app.route("/error")
def error(message="Something unexpected happened."):
    """
    route for showing error message
    """
    return render_template("error.html", error_message=message)
