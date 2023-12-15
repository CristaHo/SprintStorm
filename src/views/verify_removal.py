"""
Blueprint for handling reference and category removal verification.
"""

from flask import render_template, url_for,session,flash,redirect, request
from src.app import app
from src.utils.logging import log


@app.route("/verify_removal", methods=["POST"])
def verify_removal():
    """
    Route for verifying reference and category removal.
    """
    user_id = session.get("uid")
    if user_id is None:
        flash("Login needed to view this page")
        return redirect(url_for('login'))
    category_id = request.form["id"]
    if not category_id:
        reference_type = request.form["reference_type"]
        reference_key = request.form["reference_key"]
        log.info(f"key: {reference_key}, type: {reference_type}")
        if not (reference_type and reference_key):
            log.info("Invalid removal requested")
            return redirect(url_for('view_references'))
        else:
            log.info(f"Removal for reference {reference_key} of {reference_type} type in process")
            return render_template("verify_removal.html", remove_reference=True, reference_type=str(reference_type), reference_key=str(reference_key))
    else:
        log.info(f"Removal for category id {category_id} in process")
        return render_template("verify_removal.html", remove_category=True, category_id=category_id)
