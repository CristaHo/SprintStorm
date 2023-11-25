"""
    Book class

    Extends the Reference class
    Contains additional fields:
        - publisher
        - address
"""
from src.references.reference import Reference

class Book(Reference):
    def __init__(self, author, title, year, publisher, address):
        super().__init__(author, title, year)
        self._publisher = publisher
        self._address = address

    @property
    def author(self):
        """
        Returns the author
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author
        """
        self._author = author

    @property
    def title(self):
        """
        Returns the title
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title
        """
        self._title = title

    @property
    def year(self):
        """
        Returns the year
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Sets the year
        """
        self._year = year

    @property
    def publisher(self):
        """
        Returns the publisher
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher
        """
        self._publisher = publisher

    @property
    def address(self):
        """
        Return address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets address
        """
        self._address = address
