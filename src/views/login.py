"""
Blueprint for handling user login.
"""

from flask import render_template, request
from src.app import app
from src.db.login import get_user


@app.route("/login",methods=["GET", "POST"])
def login():
    """
    Route for logging in.
    """
    error = None
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if get_user(username, password):
            return render_template("index.html")

    return render_template("login.html", error=error)
