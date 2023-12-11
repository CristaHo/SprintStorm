"""
Handles reference things
"""
import os
from src.db import book, article

def get_all(uid):
    """
    Gets all references from database
    """
    books = book.get_all(uid)
    articles = article.get_all(uid)

    if books and articles:
        return books + articles
    return books if books else articles

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
    # path = <project_root>/static/<filename>
    path = os.getcwd() + "/static/bib-file.bib"
    with open(path,"w+", encoding="utf-8") as file:
        for line in bib_string:
            file.write(line)
    return path

def delete_one(uid:int, cite_key:str, ref_type:str):
    """
    Deletes one reference from database
    """
    if ref_type == "book":
        book.delete_one(uid, cite_key)
    elif ref_type == "article":
        article.delete_one(uid, cite_key)
    else:
        raise ValueError("Invalid reference type")
