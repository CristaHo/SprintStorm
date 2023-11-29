"""
reference.py

Module for handling references
"""
# pylint: disable=import-error, no-name-in-module
from src.references.reference import Reference
from src.references.book import Book
from src.references.article import Article
#from src.utils.database import DB

class ReferenceHandler:
    """
    Class for handling references
    """
    def __init__(self):
        self._references = []

    def create_reference(self,
        reftype: str,
        fields: dict):
        """
        Adds reference to the list
        """
        if reftype == "book":
            ref = self.create_book(fields)
        elif reftype == "article":
            ref = self.create_article(fields)
        else:
            ref = Reference(fields=fields)
            self._references.append(ref)
        return ref

    def get_references(self):
        """
        Returns the list of references
        """
        return self._references

    def get_references_in_bibtex(self):
        """
        Returns list of references in bibtex format
        """
        bibtex_list = []
        for reference in self._references:
            bibtex_list.append(reference.bibtex_str())
        return bibtex_list

    def create_book(self,fields: dict):
        """
        Module function for creating Book object
        """
        ref = Book(fields=fields)
        self._references.append(ref)
        return ref

    def create_article(self,fields: dict):
        """
        Module function for creating Article object
        """
        ref = Article(fields=fields)
        self._references.append(ref)
        return ref

reference_handler = ReferenceHandler()
