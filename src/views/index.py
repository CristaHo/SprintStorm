"""
Blueprint for handling index-page.
"""

from flask import render_template
from src.app import app

@app.route("/")
def index():
    """
    Route for viewing index-page.
    """
    return render_template("index.html")

@app.route("/ping")
def ping():
    """Returns test message"""
    return {"message": "pong"}
