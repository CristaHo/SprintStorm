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

app.config["SECRET_KEY"]= config.secret_key()

log.info("Starting application...")
log.info(f"Current environment: {config.env()}")
log.info(f"Current POSTGRES_URL: {config.db_url()}")

import src.views.index
import src.views.verify_removal
import src.views.view_reference
import src.views.add_reference
import src.views.add_category
import src.views.register
import src.views.login
import src.views.delete_user

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.port())
