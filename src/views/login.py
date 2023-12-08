"""
Blueprint for handling user login.
"""

from flask import render_template, request,flash,redirect,url_for,session
from src.app import app
from src.db.login import get_user


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

        if get_user(username, password):
            return redirect(url_for('index'))
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