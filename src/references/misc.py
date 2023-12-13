"""
    Misc class

    Extends the Reference class
    Contains additional fields:
        - url
        - urldate
"""
from src.references.reference import Reference

class Misc(Reference):
    """
        Class for misc references, extends Reference
    """
    # pylint: disable=duplicate-code
    def __init__(self, fields):
        super().__init__(
            fields={
                "key": fields['key'],
                "author":fields['author'],
                "title":fields['title'],
                "year":fields['year'],
                "category_id": fields['category_id']
                })
        self._url = fields['url']
        self._urldate = fields['urldate']

    @property
    def url(self):
        """
        Returns the url
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url
        """
        self._url = url

    @property
    def urldate(self):
        """
        Return the url date
        """
        return self._urldate

    @urldate.setter
    def urldate(self, urldate):
        """
        Sets the url date
        """
        self._urldate = urldate

    def bibtex_str(self) -> str:
        # \u007b = {
        # \u007d = }
        string = f"""@misc\u007b{self.key},
    title = \u007b{self.title}\u007d,
    author = \u007b{self.author}\u007d,
    year = \u007b{self.year}\u007d,
    url = \u007b{self.url}\u007d,
    urldate = \u007b{self._urldate}\u007d
\u007d"""
        return string
