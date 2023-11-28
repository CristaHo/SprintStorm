import unittest
from src.references.reference import Reference

class TestReference(unittest.TestCase):
    def setUp(self):
        self.reference = Reference(fields={"author":"mk", "title":"idk","year":"2001"})

    def test_author_takes_constructor_value(self):
        self.assertEqual(self.reference.author, "mk")

    def test_set_author_changes_author(self):
        self.reference.author = "lk"
        self.assertEqual(self.reference.author,"lk")

    def test_title_takes_constructor_value(self):
        self.assertEqual(self.reference.title,"idk")

    def test_set_title_changes_title(self):
        self.reference.title = "ik"
        self.assertEqual(self.reference.title, "ik")

    def test_year_takes_constructor_value(self):
        self.assertEqual(self.reference.year,"2001")

    def test_set_year_changes_year(self):
        self.reference.year = "2005"
        self.assertEqual(self.reference.year, "2005")

    def test_bibtex_str(self):
        example_str = """@reference{TODO
    title = idk
    author = mk
    year = 2001
}"""
        bibtex_str = self.reference.bibtex_str()
        self.assertEqual(bibtex_str, example_str)
