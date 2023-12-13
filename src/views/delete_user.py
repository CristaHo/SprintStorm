"""
Blueprint for handling deleting a user.
"""

from flask import redirect,url_for,flash,session
from src.app import app
from src.db.user import delete_user_by_id
from src.utils.logging import log


@app.route("/delete_user")
def delete_user():
    """
    Route for deleting a user
    """
    user_id = session.get("uid")
    if user_id:
        del session["uid"]
        delete_user_by_id(user_id)
        flash("User deleted successfully")
        return redirect(url_for('index'))

    log.error("User deletion failed. No user logged in.")
    flash("No user logged in for deletion")
    return redirect(url_for('index'))
