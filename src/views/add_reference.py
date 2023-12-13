"""
Blueprint for handling the addition of new references.
"""

from flask import request, render_template, redirect,session,flash,url_for
from src.app import app
from src.db import book, article, category
from src.utils.logging import log

@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    """
    Route for handling adding a new reference.
    """
    if request.method == "GET":
        if session.get("uid") is None:
            flash("Login needed to view this page")
            return redirect(url_for('login'))
        return render_template("add_reference.html",login_status = session.get("uid") is not None)

    if request.method == "POST":
        log.info(f"Creating reference with data: {request.form}")
        key = request.form['key']
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']
        category_id = request.form['category'] if request.form['category'] != "0" else None
        user_id = session.get("uid")

        if not user_id:
            log.error("User id was not set")
            flash("User not logged in")
            return render_template("add_reference.html")


        if request.form["reftype"] == "book":
            publisher = request.form['publisher']
            address = request.form['address']

            log.info("Inserting book into database...")
            book.insert_one({
                "key": key,
                "author": author, 
                "title": title, 
                "year": year, 
                "publisher": publisher,
                "address": address,
                "category_id": category_id,
                "user_id": user_id
                })

        if request.form["reftype"] == "article":
            journal = request.form['journal']
            volume = request.form['volume']
            pages = request.form['pages']

            log.info("Inserting article to database...")
            article.insert_one({
                "key": key,
                "author": author, 
                "title": title, 
                "year": year, 
                "journal": journal,
                "volume": volume,
                "pages": pages,
                "category_id": category_id,
                "user_id":user_id
                })

        return redirect("/view_reference")
    return redirect("/view_reference")

@app.route("/choose_reference", methods=["GET"])
def choose_reference():
    """
    Route for choosing reference type.
    """
    user_id = session.get("uid")
    choice = request.args.get('ref')
    log.info(f"Reftype \"{choice}\" chosen")
    categories = category.get_all(user_id)

    return render_template("add_reference.html", choice=choice, categories=categories)
