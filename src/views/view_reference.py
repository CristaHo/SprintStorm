from flask import Blueprint, render_template

view_reference_bp = Blueprint('view_reference', __name__)

@view_reference_bp.route("/view_reference")
def view_reference():
    """
    Route for viewing added references
    """
    reference_list = [] #Add way to get references

    return render_template("view_reference.html", references=reference_list)