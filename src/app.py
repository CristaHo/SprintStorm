"""
Defines the Flask applications dependencies and database connection.
"""

from flask import Flask
from dotenv import load_dotenv

from src.utils import config

load_dotenv()

app = Flask(__name__)
def start():
    """Starts the flaask application
    This is needed to not have circular imports
    """
    # pylint: disable=import-error, import-outside-toplevel
    from src.views.index import index_bp
    from src.views.add_reference import add_reference_bp
    from src.views.view_reference import view_reference_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(add_reference_bp)
    app.register_blueprint(view_reference_bp)

if __name__ == "__main__":
    start.run(host='0.0.0.0', port=config.port())
