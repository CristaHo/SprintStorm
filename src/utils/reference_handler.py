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
            self.create_book(
                fields['author'], fields['title'], fields['year'],
                fields['publisher'], fields['address'])
        elif reftype == "article":
            self.create_article(
                fields['author'], fields['title'], fields['year'],
                fields['journal'], fields['volume'], fields['number'],
                fields['pages'])
        else:
            ref = Reference(fields['author'], fields['title'], fields['year'])
            self._references.append(ref)
            return ref

    def get_references(self):
        """
        Returns the list of references
        """
        return self._references

    def create_book(self,
        author: str,
        title: str,
        year: str,
        publisher: str,
        address: str):
        """
        Module function for creating Book object
        """
        ref = Book(author, title, year, publisher, address)
        self._references.append(ref)
        return ref

    def create_article(self,
        author: str,
        title: str,
        year: str,
        journal: str,
        volume: str,
        number: str,
        pages: str):
        """
        Module function for creating Article object
        """
        ref = Article(author, title, year, journal, volume, number, pages)
        self._references.append(ref)
        return ref

reference_handler = ReferenceHandler()
