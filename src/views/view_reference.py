"""
Blueprint for handling viewing references.
"""

from flask import render_template, send_file,request,url_for,session,flash,redirect
from src.app import app
from src.db.reference import get_all, get_references_in_bibtex, create_bib_file
from src.db import category
from src.utils.logging import log


@app.route("/view_reference", methods=["GET", "POST"])
def view_reference():
    """
    Route for viewing added references.
    """
    user_id = session.get("uid")
    categories = category.get_all(user_id)
    reference_list = get_all(user_id)
    if request.method == "GET":
        if user_id is None:
            flash("Login needed to view this page")
            return redirect(url_for('login'))

        log.info(f"All references: {reference_list}")
        return render_template("view_reference.html",
                               references=reference_list, categories = categories)
    if request.method == "POST":
        cat = request.form["category"]

        reference_list = [ref for ref in reference_list if ref.category_id == int(cat)]

        log.info(f"References for category: {reference_list}")

        return render_template("view_reference.html",
                               references=reference_list, categories=categories)

    return None


@app.route("/view_reference/download")
def downloader_bib():
    """
    Route for downloading .bib file
    """
    if session.get("uid") is None:
        flash("Login needed")
        return redirect(url_for('login'))
    log.info("Creating BibTeX file...")
    bib_list = get_references_in_bibtex(get_all(session.get("uid")))
    path = create_bib_file(bib_list)
    log.info(f"Created {bib_list} to path {path}")
    return send_file(path, as_attachment = True)
