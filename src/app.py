"""
Defines the Flask applications dependencies and database connection.
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views.add_reference import add_reference_bp
from views.view_reference import view_reference_bp

if os.environ.get('ENVIRONMENT') == 'production':
    sql_url = os.environ.get('POSTGRES_URL') or None
else:
    sql_url = os.environ.get('TEST_POSTGRES_URL') or None
if sql_url is None:
    raise RuntimeError("No SQL URL was found. Connection cannot be made.")


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = sql_url
db = SQLAlchemy(app)
app.register_blueprint(add_reference_bp)
app.register_blueprint(view_reference_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
