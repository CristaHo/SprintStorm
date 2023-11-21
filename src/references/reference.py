"""
    Parent class for references

    Contains reference fields: Author, Title and Year.
"""

class Reference:

    def __init__(self, author, title, year):
        self._author = author
        self._title = title
        self._year = year

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year
