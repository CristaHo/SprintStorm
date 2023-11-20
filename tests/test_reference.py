import unittest
from src.references.reference import Reference


class TestReference(unittest.TestCase):
    def setUp(self):
        self.reference = Reference(author = "mk", title="idk",year = "2001")

    def test_author_takes_constructor_value(self):
        self.assertEqual(self.reference.get_author(), "mk")

    def test_set_author_changes_author(self):
        self.reference.set_author("lk")
        self.assertEqual(self.reference.get_author(),"lk")

    def test_title_takes_constructor_value(self):
        self.assertEqual(self.reference.get_title(),"idk")

    def test_set_title_changes_title(self):
        self.reference.set_title("ik")
        self.assertEqual(self.reference.get_title(), "ik")

    def test_year_takes_constructor_value(self):
        self.assertEqual(self.reference.get_year(),"2001")

    def test_set_year_changes_year(self):
        self.reference.set_year("2005")
        self.assertEqual(self.reference.get_year(), "2005")
