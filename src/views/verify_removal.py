"""
Blueprint for handling reference and category removal verification.
"""

from flask import render_template, url_for,session,flash,redirect, request
from src.app import app
from src.utils.logging import log


@app.route("/verify_removal/reference", methods=["POST"])
def verify_reference_removal():
    """
    Route for verifying reference removal.
    """
    user_id = session.get("uid")
    if user_id is None:
        flash("Login needed to view this page")
        return redirect(url_for('login'))
    reference_type = request.form["reference_type"]
    reference_key = request.form["reference_key"]
    if not (reference_key or reference_type):
        log.info("Invalid removal requested")
        return redirect(url_for('view_references'))
    log.info(f"Removal for reference {reference_key} of {reference_type} type in process")
    return render_template("reference_removal.html",\
        remove_reference=True,\
        reference_type=str(reference_type),\
        reference_key=str(reference_key))

@app.route("/verify_removal/category", methods=["POST"])
def verify_category_removal():
    """
    Route for verifying category removal.
    """
    user_id = session.get("uid")
    if user_id is None:
        flash("Login needed to view this page")
        return redirect(url_for('login'))
    category_id = request.form["id"]
    if not category_id:
        log.info("Invalid removal requested")
        return redirect(url_for('add_category'))
    log.info(f"Removal for category id {category_id} in process")
    return render_template("category_removal.html",\
        remove_category=True,\
        category_id=category_id)
