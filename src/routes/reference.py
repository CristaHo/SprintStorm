from app import app
from flask import request, render_template

@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    if request.method == "GET":
        return render_template(
            "add_reference.html"
        )

    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']