"""
Defines how the app is run fly.io.
In general you should not need to touch this if CI/CD works.
"""

# these pylint warnings are ignored because these errors
# are not "correct". This file is launced by gunicorn
# and not with python as usually, therefore the errors
# don't apply

# pylint: disable=import-error, no-name-in-module
from src.app import app

if __name__ == "__main__":
    app.run()
