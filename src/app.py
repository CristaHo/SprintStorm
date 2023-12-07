"""
Defines the Flask applications dependencies and database connection.
"""
#pylint: disable=unused-import, wrong-import-position
from flask import Flask
from dotenv import load_dotenv

from src.utils import config
from src.utils.logging import log

load_dotenv()

app = Flask(__name__)

log.info("Starting application...")
log.info(f"Current environment: {config.env()}")
log.info(f"Current POSTGRES_URL: {config.db_url()}")

@app.route("/ping")
def ping():
    """Returns test message"""
    return {"message": "pong"}

import src.views.index
import src.views.view_reference
import src.views.add_reference
import src.views.register_user

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.port())
