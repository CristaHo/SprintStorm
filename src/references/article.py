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
    # pylint: disable=duplicate-code
    def __init__(self, fields):
        super().__init__(
            fields={
                "key": fields['key'],
                "author":fields['author'],
                "title":fields['title'],
                "year":fields['year'],
                "category_id":fields['category_id']
                })
        self._journal = fields['journal']
        self._volume = fields['volume']
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

    def bibtex_str(self) -> str:
        # \u007b = {
        # \u007d = }
        return f"""@article\u007b{self.key}
    title = {self.title}
    author = {self.author}
    year = {self.year}
    journal = {self.journal}
    volume = {self.volume}
    pages = {self.pages}
\u007d"""
