"""
Blueprint for handling index-page.
"""

from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def index():
    """
    Route for viewing index-page.
    """
    return render_template("index.html")
