"""
Handles reference things
"""
import os
from src.db import book, article, misc

def get_all(uid):
    """
    Gets all references from the database
    """
    collections = {
        "books": book.get_all(uid),
        "articles": article.get_all(uid),
        "miscs": misc.get_all(uid)
    }

    return collections

def get_references_in_bibtex(references):
    """
    Returns list of references in bibtex format as string
    """
    values = []
    for reference, value in references.items():
        if references[reference]:
            values += value

    bibtex_list_string = '\n\n'.join(ref.bibtex_str() for ref in values)
    return bibtex_list_string

def create_bib_file(bib_string):
    """
    Creates .bib file from references to static folder
    """
    # path = <project_root>/static/<filename
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
