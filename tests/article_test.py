import unittest
from src.references.article import Article

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.reference = Article(
            author = "mk", title="idk",year = "2001",
            journal = "journal", volume = "volume",
            number = "number", pages = "pages")

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

    def test_get_type_returns_article(self):
        type_as_string = str(type(self.reference))
        self.assertIn("class", type_as_string)
        self.assertIn("article", type_as_string)
        self.assertIn("Article", type_as_string)

    def test_journal_takes_constructor_value(self):
        self.reference.journal = "journal"
        self.assertEqual(self.reference.journal, "journal")

    def test_set_journal_changes_journal(self):
        self.reference.journal = "journal2"
        self.assertEqual(self.reference.journal, "journal2")

    def test_volume_takes_constructor_value(self):
        self.reference.volume = "volume"
        self.assertEqual(self.reference.volume, "volume")

    def test_set_volume_changes_volume(self):
        self.reference.volume = "volume2"
        self.assertEqual(self.reference.volume, "volume2")

    def test_number_takes_constructor_value(self):
        self.reference.number = "number"
        self.assertEqual(self.reference.number, "number")

    def test_set_number_changes_number(self):
        self.reference.number = "number2"
        self.assertEqual(self.reference.number, "number2")

    def test_pages_takes_constructor_value(self):
        self.reference.pages = "pages"
        self.assertEqual(self.reference.pages, "pages")

    def test_set_pages_changes_pages(self):
        self.reference.pages = "pages2"
        self.assertEqual(self.reference.pages, "pages2")
