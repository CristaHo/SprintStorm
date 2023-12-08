"""
File to handle adding/deleting category route
"""

from flask import request, render_template, redirect,session
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
        categories = category.get_all(user_id) or []
        log.info(f"All users categories: {categories}")

        return render_template("add_category.html", categories=categories)

    if request.method == "POST":
        log.info(f"Creating category with data: {request.form['name']}")
        name = request.form["name"]
        log.info("Inserting category into database...")
        category.insert_one({"name":name,
                             "user_id":user_id})

    return redirect("/add_category")

@app.route("/delete_category", methods=["POST"])
def delete_category():
    """
    Route for deleting categories
    """
    category_id = request.form["id"]
    log.info(f"Deleting category with id: {category_id} from database...")
    category.delete_one({"id":category_id})

    return redirect("/add_category")
