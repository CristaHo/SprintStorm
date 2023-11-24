"""
Blueprint for handling viewing references.
"""

from flask import Blueprint, render_template
from src.utils.reference_handler import get_references

view_reference_bp = Blueprint('view_reference', __name__)

@view_reference_bp.route("/view_reference")
def view_reference():
    """
    Route for viewing added references.
    """
    reference_list = get_references() #Add way to get references

    return render_template("view_reference.html", references=reference_list)
