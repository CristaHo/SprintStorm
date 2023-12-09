"""
Blueprint for handling user login.
"""

from flask import render_template, request,flash,redirect,url_for,session
from src.app import app
from src.db.login import check_user
from src.utils.logging import log


@app.route("/login",methods=["GET", "POST"])
def login():
    """
    Route for logging in.
    """
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            log.error("Username or password missing")
            flash("Username or password not provided")
        elif check_user(username, password):
            log.info("User successfully logged in")
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password")

    return render_template("login.html")

@app.route("/logout")
def logout():
    """
    Route for logging out.
    """
    if session.get("uid") is not None:
        del session["uid"]
        flash("You have logged out")
    return redirect(url_for('index'))
