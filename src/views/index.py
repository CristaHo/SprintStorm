"""
Blueprint for handling index-page.
"""

from flask import render_template,session
from src.app import app

@app.route("/")
def index():
    """
    Route for viewing index-page.
    """
    return render_template("index.html",login_status = session.get("uid") is not None)

@app.route("/ping")
def ping():
    """Returns test message"""
    return {"message": "pong"}
