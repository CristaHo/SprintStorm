"""
Utility to read and provide environmental variables
"""
import os

def read_postgres_url():
    """
    Reads the POSTGRES_URL from the environment
    Returns postgres url, if url for corresponting environment is found.
    If environment and url do not match or url is missing, returns None
    """
    sql_url = os.environ.get('POSTGRES_URL') \
        if os.environ.get('ENVIRONMENT') == 'production' \
        else os.environ.get('TEST_POSTGRES_URL')
    return sql_url or None