"""
Blueprint for handling registering a new user.
"""

from flask import render_template, request,redirect,url_for,flash,session
from src.app import app
from src.db.register import insert_new_user
from src.utils.logging import log


@app.route("/register",methods=["GET", "POST"])
def register():
    """
    Route for registering a new user.
    """
    error = None
    if request.method == "GET":
        if session.get("uid") is not None:
            return redirect(url_for('index'))
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password1"]
        password_confirmation = request.form["password2"]

        if not username or not password or not password_confirmation:
            log.error("All fields not given")
            error = "All fields not given"

        elif password != password_confirmation:
            log.error("Password and confirmation don't match")
            error = "Passwords don't match"

        elif insert_new_user(username, password):
            log.info("User created")
            flash("User created")
            return redirect(url_for('index'))

        else:
            error = "Error in user creation"

    return render_template("register.html", error=error)
