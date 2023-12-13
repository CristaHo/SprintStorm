"""
File to handle adding/deleting category route
"""

from flask import request, render_template, redirect, session, flash,url_for
from src.app import app
from src.db import category
from src.utils.logging import log

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Route to handle adding a new category
    """
    user_id = session.get("uid")
    if request.method == "GET":
        if session.get("uid") is None:
            flash("Login needed to view this page")
            return redirect(url_for('login'))
        categories = category.get_all(user_id)
        log.info(f"All users categories: {categories}")

        return render_template("add_category.html", categories=categories,
                               login_status = session.get("uid") is not None)

    if request.method == "POST":
        name = request.form["name"]

        if not user_id:
            log.error("User_id is not set")
            flash("User not logged in")
            return render_template("add_category.html", categories=category.get_all(user_id))
        if not name:
            flash("Category name not set")
            log.error("Category name not set")
            return render_template("add_category.html", categories=category.get_all(user_id))

        log.info(f"Creating category with data: {request.form['name']} {user_id}")
        category.insert_one({"name":name,
                             "user_id":user_id})

    return render_template("add_category.html", categories=category.get_all(user_id))

@app.route("/delete_category", methods=["POST"])
def delete_category():
    """
    Route for deleting categories
    """
    category_id = request.form["id"]
    if not category_id:
        log.error("Category id not set")
        flash("Category id not set")
        return redirect("/add_category")

    log.info(f"Deleting category with id: {category_id} from database...")
    category.delete_one({"id":category_id})

    return redirect("/add_category")
