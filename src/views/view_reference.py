"""
Blueprint for handling viewing references.
"""

from flask import render_template, send_file
from src.app import app
from src.db.reference import get_all, get_references_in_bibtex, create_bib_file


@app.route("/view_reference")
def view_reference():
    """
    Route for viewing added references.
    """
    reference_list = get_all()

    return render_template("view_reference.html", references=reference_list)

@app.route("/view_reference/download")
def downloader_bib():
    """
    Route for downloading .bib file
    """
    bib_list = get_references_in_bibtex(get_all())
    path = create_bib_file(bib_list)
    return send_file(path, as_attachment = True)
