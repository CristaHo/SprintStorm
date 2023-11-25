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
    Article class
    """
    def __init__(self, author, title, year, journal, volume, number, pages):
        super().__init__(author, title, year)
        self._journal = journal
        self._volume = volume
        self._number = number
        self._pages = pages

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
