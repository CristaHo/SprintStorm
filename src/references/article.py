"""
    Article class

    Extends the Reference class
    Contains additional fields:
        - journal
        - volume
        - number
        - pages
"""
from sqlalchemy.ext.hybrid import hybrid_property
from src.references.reference import Reference
from src.utils.database import db

class Article(Reference):
    """
        Class for article references, extends Reference
    """
    __tablename__ = 'article'

    id = db.Column(db.Integer, db.ForeignKey('reference.id'), primary_key=True)
    _journal = db.Column(db.String(255), name='journal')
    _volume = db.Column(db.Integer, name='volume')
    _pages = db.Column(db.String(255), name='pages')

    def __init__(self, fields):
        """
        Extends Reference
        journal: Journal the article was published in
        volume: Volume of the article
        number: number of the article
        pages: On which pages the article is
        """
        super().__init__(
            fields={"author":fields['author'],
                    "title":fields['title'],
                    "year":fields['year']})
        self._journal = fields['journal']
        self._volume = fields['volume']
        self._pages = fields['pages']

    @staticmethod
    def get_all():
        "Return all articles from table"
        rows = Article.query.all()
        return rows

    @staticmethod
    def insert_one(article):
        "Inserts one article into db"
        db.session.add(article)
        db.session.commit()


    @hybrid_property
    def journal(self):
        """
        Getter for journal
        """
        return self._journal

    @journal.setter
    def journal(self, value):
        """
        Setter for journal
        """
        self._journal = value

    @hybrid_property
    def volume(self):
        """
        Getter for volume
        """
        return self._volume

    @volume.setter
    def volume(self, value):
        """
        Setter for volume
        """
        self._volume = value

    @hybrid_property
    def pages(self):
        """
        Getter for pages
        """
        return self._pages

    @pages.setter
    def pages(self, value):
        """
        Setter for pages
        """
        self._pages = value
        