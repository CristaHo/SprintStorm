"""
    Article class

    Extends the Reference class
    Contains additional fields:
        - journal
        - volume
        - number
        - pages
"""
from src.references.reference import Reference

class Article(Reference):
    """
        Class for article references, extends Reference
    """
    def __init__(self, fields):
        super().__init__(
            fields={"author":fields['author'],
                    "title":fields['title'],
                    "year":fields['year']})
        self._journal = fields['journal']
        self._volume = fields['volume']
        self._number = fields['number']
        self._pages = fields['pages']

    @property
    def journal(self):
        """
        Returns the journal
        """
        return self._journal

    @journal.setter
    def journal(self, journal):
        """
        Sets the journal
        """
        self._journal = journal

    @property
    def volume(self):
        """
        Return volume
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """
        Sets volume
        """
        self._volume = volume

    @property
    def number(self):
        """
        returns number
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets number
        """
        self._number = number

    @property
    def pages(self):
        """
        returns pages
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets pages
        """
        self._pages = pages
