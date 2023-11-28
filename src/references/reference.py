"""
    Parent class for references

    Contains reference fields: Author, Title and Year.
"""
from sqlalchemy.ext.hybrid import hybrid_property
from src.utils.database import db

class Reference(db.Model):
    """
    Parent class for references
    """
    __tablename__ = 'reference'

    id = db.Column(db.Integer, primary_key=True)
    _author = db.Column(db.String(255), name='author')
    _title = db.Column(db.String(255), name='title')
    _year = db.Column(db.Integer, name='year')

    def __init__(self, fields: dict):
        """
        author: author of the reference
        title: title of the reference
        year: year when reference was published
        """
        self._author = fields['author']
        self._title = fields['title']
        self._year = fields['year']

    @staticmethod
    def get_all():
        "Returns all References from table"
        rows = Reference.query.all()
        return rows

    @staticmethod
    def insert_one(reference):
        "Inserts one reference into db"
        db.session.add(reference)
        db.session.commit()

    @hybrid_property
    def author(self):
        """
        Getter for author
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Setter for author
        """
        self._author = author

    @hybrid_property
    def title(self):
        """
        Getter for title
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Setter for title
        """
        self._title = title

    @hybrid_property
    def year(self):
        """
        Getter for year
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Setter for year
        """
        self._year = year
