"""
    Parent class for references

    Contains reference fields: Author, Title and Year.
"""

class Reference:
    """
    Parent class for references
    """
    def __init__(self, author, title, year):
        """
        author: author of the refernce
        title: title of the reference
        year: year when reference was published
        """
        self._author = author
        self._title = title
        self._year = year

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
        Return title
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets title
        """
        self._title = title

    @property
    def year(self):
        """
        returns year
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Sets year
        """
        self._year = year
