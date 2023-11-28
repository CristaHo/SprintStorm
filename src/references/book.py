"""
    Book class

    Extends the Reference class
    Contains additional fields:
        - publisher
        - address
"""
from sqlalchemy.ext.hybrid import hybrid_property
from src.references.reference import Reference
from src.utils.database import db

class Book(Reference):
    """
        Class for book references, extends Reference
    """
    __tablename__ = 'book'

    id = db.Column(db.Integer, db.ForeignKey('reference.id'), primary_key=True)
    _publisher = db.Column(db.String(255), name='publisher')

    def __init__(self, fields):
        """
        Extends Refernce
        publisher: publisher of the book
        address: address of the book"""
        super().__init__(
            fields={"author":fields['author'],
                    "title":fields['title'],
                    "year":fields['year']})
        self._publisher = fields['publisher']

    @staticmethod
    def get_all():
        "Return all Books from table"
        rows = Book.query.all()
        return rows

    @staticmethod
    def insert_one(book):
        "Inserts one book into db"
        db.session.add(book)
        db.session.commit()

    @hybrid_property
    def publisher(self):
        """
        Getter for publisher
        """
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        """
        Setter for publisher
        """
        self._publisher = value
