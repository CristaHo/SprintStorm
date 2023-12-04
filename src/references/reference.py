"""
    Parent class for references

    Contains reference fields: Author, Title and Year.
"""

class Reference:
    """
    Parent class for references
    """
    def __init__(self, fields: dict):
        """
        author: author of the refernce
        title: title of the reference
        year: year when reference was published
        """
        self._user_key = fields['key']
        self._author = fields['author']
        self._title = fields['title']
        self._year = fields['year']

    @property
    def key(self):
        """
        Returns the author
        """
        return self._user_key

    @key.setter
    def key(self, key):
        """
        Sets the author
        """
        self._user_key = key

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

    def bibtex_str(self) -> str:
        """Creates a BibTeX formatted string of the reference

        :returns: Class object as a string, formatted as BibTeX entry
        """
        # \u007b = {
        # \u007d = }
        return f"""@reference\u007b{self.key}
    title = {self.title}
    author = {self.author}
    year = {self.year}
\u007d"""
