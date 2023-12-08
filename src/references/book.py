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
                "year":fields['year'],
                "category_id": fields['category_id']
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
        string = f"""@book\u007b{self.key},
    title = \u007b{self.title}\u007d,
    author = \u007b{self.author}\u007d,
    year = \u007b{self.year}\u007d,
    publisher = \u007b{self.publisher}\u007d
\u007d"""
        return string
