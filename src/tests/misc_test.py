import unittest
from src.references.misc import Misc

class TestMisc(unittest.TestCase):
    def setUp(self):
        self.reference = Misc(fields={
            "key": "Someuniquekey", "author": "test", "title": "test_title",
            "year": "2023", "url": "https://www.wikipedia.com", 
            "urldate": "13.12.2023", "category_id":1
        })

    def test_author_takes_constructor_value(self):
        self.assertEqual(self.reference.author, "test")

    def test_set_author_changes_author(self):
        self.reference.author = "test_2"
        self.assertEqual(self.reference.author,"test_2")

    def test_title_takes_constructor_value(self):
        self.assertEqual(self.reference.title,"test_title")

    def test_set_title_changes_title(self):
        self.reference.title = "test_title_2"
        self.assertEqual(self.reference.title, "test_title_2")

    def test_year_takes_constructor_value(self):
        self.assertEqual(self.reference.year,"2023")

    def test_set_year_changes_year(self):
        self.reference.year = "2001"
        self.assertEqual(self.reference.year, "2001")

    def test_get_type_returns_article(self):
        self.assertIsInstance(self.reference, Misc)

    def test_category_id_takes_constructor_value(self):
        self.assertEqual(self.reference.category_id, 1)

    def test_category_id_changes_constructor_value(self):
        self.reference.category_id = 2
        self.assertEqual(self.reference.category_id, 2)

    def test_url_takes_constructor_value(self):
        self.assertEqual(self.reference.url, "https://www.wikipedia.com")

    def test_set_url_changes_url(self):
        self.reference.url = "https://www.is.fi"
        self.assertEqual(self.reference.url, "https://www.is.fi")

    def test_urldate_takes_constructor_value(self):
        self.assertEqual(self.reference.urldate, "13.12.2023")

    def test_set_urldate_changes_url(self):
        self.reference.urldate = "9.11.2023"
        self.assertEqual(self.reference.urldate, "9.11.2023")

    def test_bibtex_str(self):
        example_str = """@misc{Someuniquekey,
    title = \u007btest_title\u007d,
    author = \u007btest\u007d,
    year = \u007b2023\u007d,
    url = \u007bhttps://www.wikipedia.com\u007d,
    urldate = \u007b13.12.2023\u007d
}"""
        bibtex_str = self.reference.bibtex_str()
        self.assertEqual(bibtex_str, example_str)