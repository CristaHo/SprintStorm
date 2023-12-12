from unittest import TestCase
from sqlalchemy import text

from src.app import app

class RegisterDatabaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

    def test_register_new_correct_user(self):
        with app.app_context():
            from src.db import register
            from src.utils.database import db
            pre_result = db.session.execute(text("SELECT * FROM users")).fetchall()
            register.insert_new_user("martti", "unsecure")
            result = db.session.execute(text("SELECT * FROM users")).fetchall()

        self.assertEqual(pre_result, [])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[0][1], "martti")

    def test_register_new_duplicate_user(self):
        with app.app_context():
            from src.db import register
            pre_result = register.insert_new_user("martti", "unsecure")
            result = register.insert_new_user("martti", "unsecure2")
        
        self.assertEqual(pre_result, True)
        self.assertEqual(result, False)
