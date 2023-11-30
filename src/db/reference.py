"""
Handles reference things
"""
from src.db import book, article

def get_all():
    """
    Gets all references from database
    """
    books = book.get_all()
    articles = article.get_all()

    return books + articles

def get_references_in_bibtex(references):
    """
    Returns list of references in bibtex format as string
    """
    bibtex_list_string = '\n\n'.join(reference.bibtex_str() for reference in references)
    return bibtex_list_string
