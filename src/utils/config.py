"""
Here is defined all of the values read from environment variables
"""

from os import getenv
from src.utils.logging import log

ENV_OPTIOS = ["production", "development", "staging", "test"]

def db_url() -> str:
    """Returns the current database url as defined in environment variables

    :returns: database url
    """

    if env() == "production":
        url = getenv("POSTGRES_URL")
    else:
        url = getenv("TEST_POSTGRES_URL")

    if not url:
        raise RuntimeError("No POSTGRES_URL defined")
    return str(url)

def env() -> str:
    """Returns the current environment as defined in environment variables

    :returns: current environment, one of ENV_OPTIONS, defaults to production
    """

    curr_env = getenv("ENVIRONMENT")
    if not curr_env or curr_env not in ENV_OPTIOS:
        log.debug("ENVIRONMENT not set or incorrect, defaulting to \"production\"...")
        curr_env = "production"
    return str(curr_env)

def port() -> int:
    """Returns the port, defaults to 3000 if no other value is defined

    NOTE: does not affect Procfile, only local development

    :returns: port number read from PORT env var, otherwise defaults to 3000"""

    port_num = getenv("PORT")

    if not port_num:
        return 3000

    try:
        return int(port_num)

    # handle incorrect value and None
    except (ValueError, TypeError):
        return 3000

def secret_key() -> str:
    """ Returns secret key from env
    """
    secret_key = getenv("SECRET_KEY")
    
    if not secret_key:
        return "testkey"
    return secret_key
