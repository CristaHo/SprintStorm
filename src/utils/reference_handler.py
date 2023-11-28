"""
reference.py

Module for handling references
"""
# pylint: disable=import-error, no-name-in-module
from src.references.reference import Reference
from src.references.book import Book
from src.references.article import Article

class ReferenceHandler:
    """
    Class for handling references
    """
    def __init__(self):
        self._references = []

    def create_reference(self, reftype: str, fields: dict):
        """
        Adds reference to the list
        """
        if reftype == "book":
            ref = self.create_book(fields)
        elif reftype == "article":
            ref = self.create_article(fields)
        else:
            ref = Reference(fields)
            Reference.insert_one(ref)

        return ref

    def get_references(self):
        """
        Returns the list of references
        """
        if len(Reference.get_all()) > 0:
            for i in Reference.get_all():
                self._references.append(i)
        if len(Book.get_all()) > 0:
            for i in Book.get_all():
                self._references.append(i)
        if len(Article.get_all()) > 0:
            for i in Article.get_all():
                self._references.append(i)
        return self._references

    def create_book(self, fields: dict):
        """
        Module function for creating Book object
        """
        book = Book(fields)
        Book.insert_one(book)
        return book

    def create_article(self, fields: dict):
        """
        Module function for creating Article object
        """
        article = Article(fields)
        Article.insert_one(article)
        return article

reference_handler = ReferenceHandler()
