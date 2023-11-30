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

def create_bib_file(bib_string):
        """
        Creates .bib file from references to static folder
        """
        path = "static/bib-file.bib"
        with open(path,"w+", encoding="utf-8") as file:
            for line in bib_string:
                file.write(line)
        return path
