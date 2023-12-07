from unittest import TestCase

from src.app import app

class CategoryDatabaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

    def test_category_get_all_returns_None_if_no_categories_in_database(self):
        with app.app_context():
            from src.db import category, register
            register.insert_new_user('test', 'test')
            result = category.get_all(1)
        self.assertEqual(result, [])

    def test_category_inser_one(self):
        test_category = {"name":"123",
                         "user_id":1}
        with app.app_context():
            from src.db import category, register
            register.insert_new_user('test', 'test')
            pre_result = category.get_all(1)
            category.insert_one(test_category)
            result = category.get_all(1)

        if result:
            self.assertEqual(pre_result, [])
            self.assertEqual(result[0].name, "123")
            self.assertEqual(result[0].user_id, 1)
        else:
            raise AssertionError("No result from database")