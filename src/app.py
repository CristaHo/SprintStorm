"""
Defines the Flask applications dependencies and database connection.
"""

from flask import Flask
from dotenv import load_dotenv

from views.index import index_bp
from views.add_reference import add_reference_bp, choose_reference_bp
from views.view_reference import view_reference_bp
from utils import config

load_dotenv()

app = Flask(__name__)

@app.route("/ping")
def ping():
    return {"message": "pong"}

app.register_blueprint(index_bp)
app.register_blueprint(add_reference_bp)
app.register_blueprint(choose_reference_bp)
app.register_blueprint(view_reference_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.port())
