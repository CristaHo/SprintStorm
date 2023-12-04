"""
    Book class

    Extends the Reference class
    Contains additional fields:
        - publisher
        - address
"""
from src.references.reference import Reference

class Book(Reference):
    """
        Class for book references, extends Reference
    """
    def __init__(self, fields):
        super().__init__(
            fields={
                "key": fields['key'],
                "author":fields['author'],
                "title":fields['title'],
                "year":fields['year']
                })
        self._publisher = fields['publisher']

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

    def bibtex_str(self) -> str:
        # \u007b = {
        # \u007d = }
        string = f"""@book\u007b{self.key}
    title = {self.title}
    author = {self.author}
    year = {self.year}
    publisher = {self.publisher}
\u007d"""
        return string
