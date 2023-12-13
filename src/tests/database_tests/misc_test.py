from unittest import TestCase

from src.app import app
from src.references.misc import Misc

class MiscDatabaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

    def test_misc_get_all_returns_None_if_no_miscs_in_database(self):
        with app.app_context():
            from src.db import misc,register
            register.insert_new_user("mie","123")
            result = misc.get_all(1)
        self.assertEqual(result, None)

    def test_misc_insert_one_with_correct_object_is_correctly_saved_to_db(self):
        test_misc = {
            "key": "key",
            "author": "Me",
            "title": "wikipedia", 
            "year": 2023,
            "url": "https://www.wikipedia.com", 
            "urldate": "13.12.2023",
            "category_id":1,
            "user_id":1
        }

        with app.app_context():
            from src.db import misc, register, category
            register.insert_new_user('test', 'test')
            category.insert_one({"name":"test", "user_id":1})
            pre_result = misc.get_all(1)
            misc.insert_one(test_misc)
            result = misc.get_all(1)

        if result:
            self.assertEqual(pre_result, None)
            self.assertIsInstance(result[0], Misc)

            self.assertEqual(result[0].key, "key")
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result[0].title, "wikipedia")
            self.assertEqual(result[0].year, 2023)
            self.assertEqual(result[0].url, "https://www.wikipedia.com")
            self.assertEqual(result[0].urldate, "13.12.2023")
        else:
            raise AssertionError("No result from database")

    def test_misc_get_all_multiple_references_returns_all(self):
        test_misc = {
            "key": "key",
            "author": "Me",
            "title": "wikipedia", 
            "year": 2023,
            "url": "https://www.wikipedia.com", 
            "urldate": "13.12.2023",
            "category_id":1,
            "user_id":1
        }

        other_test_misc = {
            "key": "key",
            "author": "You",
            "title": "wikipedia2", 
            "year": 2023,
            "url": "https://www.wikipedia.com", 
            "urldate": "13.12.2023",
            "category_id":2,
            "user_id":1
        }

        with app.app_context():
            from src.db import misc, register, category
            register.insert_new_user('test', 'test')
            category.insert_one({"name":"test", "user_id":1})
            category.insert_one({"name":"test2", "user_id":1})
            misc.insert_one(test_misc)
            misc.insert_one(other_test_misc)
            result = misc.get_all(1)

        if result:
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result[1].author, "You")
        else:
            raise AssertionError("No result from database")

    def test_misc_different_users_get_their_own_references(self):
        test_misc = {
            "key": "key",
            "author": "Me",
            "title": "wikipedia", 
            "year": 2023,
            "url": "https://www.wikipedia.com", 
            "urldate": "13.12.2023",
            "category_id":1,
            "user_id":1
        }

        other_test_misc = {
            "key": "key",
            "author": "You",
            "title": "wikipedia2", 
            "year": 2023,
            "url": "https://www.wikipedia.com", 
            "urldate": "13.12.2023",
            "category_id":2,
            "user_id":2
        }

        with app.app_context():
            from src.db import misc, register, category
            register.insert_new_user('test', 'test')
            register.insert_new_user('test2', 'test')
            category.insert_one({"name":"test", "user_id":1})
            category.insert_one({"name":"test2", "user_id":2})
            misc.insert_one(test_misc)
            misc.insert_one(other_test_misc)
            result = misc.get_all(1)
            result2 = misc.get_all(2)

        if result:
            self.assertEqual(len(result), 1)
            self.assertEqual(len(result2), 1)
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result2[0].author, "You")
        else:
            raise AssertionError("No result from database")

    def test_delete_one_misc(self):
        test_misc = {
            "key": "key",
            "author": "Me",
            "title": "wikipedia", 
            "year": 2023,
            "url": "https://www.wikipedia.com", 
            "urldate": "13.12.2023",
            "category_id":1,
            "user_id":1
        }

        with app.app_context():
            from src.db import misc, register, category
            register.insert_new_user('test', 'test')
            category.insert_one({"name":"test", "user_id":1})
            misc.insert_one(test_misc)
            result = misc.get_all(1)
            misc.delete_one(1,"key")
            result2 = misc.get_all(1)

        if result:
            self.assertEqual(result2, None)
        else:
            raise AssertionError("No result from database")