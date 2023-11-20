"""
Defines the Flask's app object.

Contains also a test endpoint.
"""
from flask import Flask


app = Flask(__name__)

@app.route("/test")
def hello_world():
    """
    A basic endpoint to test the app
    """

    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
