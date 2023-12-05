"""
Blueprint for handling the addition of new references.
"""

from flask import request, render_template, redirect
from src.app import app
from src.db import book, article
from src.utils.logging import log

@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    """
    Route for handling adding a new reference.
    """
    if request.method == "GET":
        return render_template("add_reference.html")

    if request.method == "POST":
        log.info(f"Creating user with data: {request.form}")
        key = request.form['key']
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']
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
                "address": address
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
                "pages": pages
                })

        return redirect("/view_reference")

    log.warn("No correct method given for request")
    return None

@app.route("/choose_reference", methods=["GET"])
def choose_reference():
    """
    Route for choosing reference type.
    """
    choice = request.args.get('ref')
    log.info(f"Reftype \"{choice}\" chosen")

    return render_template("add_reference.html", choice=choice)
