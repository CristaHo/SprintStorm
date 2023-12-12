from unittest import TestCase

from src.app import app

class LoginDatabaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

    def test_login_correct_user(self):
        with app.app_context():
            from src.db import register, login
            register.insert_new_user("martti", "unsecure")
            result = login.get_user("martti")
        if result:
            self.assertEqual(result[0], 1) # id of the user
            self.assertEqual(result[2], "martti")
        else:
            raise AssertionError("Database didn't return anything when it should have")

    def test_login_incorrect_user(self):
        with app.app_context():
            from src.db import register, login
            register.insert_new_user("martti", "unsecure")
            result = login.get_user("manaatti")
        self.assertEqual(result, None)
