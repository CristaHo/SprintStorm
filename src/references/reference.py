"""
    Parent class for references

    Contains reference fields: Author, Title and Year.
"""

class Reference:

    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def set_author(self, author):
        self.author = author

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def get_author(self):
        return self.author
    
    def get_title(self):
        return self.title

    def get_year(self):
        return self.year
