"""
Utility to read and provide environmental variables
"""
import os

def read_postgres_url():
    """
    Reads the POSTGRES_URL from the environment
    """
    if os.environ.get('ENVIRONMENT') == 'production':
        sql_url = os.environ.get('POSTGRES_URL') or None
    else:
        sql_url = os.environ.get('TEST_POSTGRES_URL') or None
    return sql_url