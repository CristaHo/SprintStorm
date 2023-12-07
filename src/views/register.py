"""
Blueprint for handling registering a new user.
"""

from flask import render_template, request
from src.app import app
from src.db.register import insert_new_user


@app.route("/register",methods=["GET", "POST"])
def register():
    """
    Route for registering a new user.
    """
    error = None
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password1"]
        password_confirmation = request.form["password2"]

        if password != password_confirmation:
            error = "Passwords don't match"

        elif insert_new_user(username, password):
            return render_template("index.html")

    return render_template("register.html", error=error)
