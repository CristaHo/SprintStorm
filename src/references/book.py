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
