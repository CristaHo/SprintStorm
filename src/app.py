"""
Defines the Flask applications dependencies and database connection.
"""

from flask import Flask
from views.index import index_bp
from views.add_reference import add_reference_bp
from views.view_reference import view_reference_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(add_reference_bp)
app.register_blueprint(view_reference_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
