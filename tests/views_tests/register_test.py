from unittest import TestCase
from sqlalchemy import text
from src.app import app

class TestRegister(TestCase):
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

    def test_register_page_is_correct(self):
        response = self.app.get("/register")
        self.assertTrue(b'Username:' in response.data)
        self.assertTrue(b'Password:' in response.data)
        self.assertTrue(b'Confirm password:' in response.data)

    def test_register_new_correct_user(self):
        test_user = {
                "username": "test",
                "password1": "1234",
                "password2": "1234"
                }

        # empty database
        with app.app_context():
            from src.utils.database import db
            sql = text("SELECT username FROM users")
            pre_result = db.session.execute(sql).fetchone()
            self.assertEqual(pre_result, None)

        # user is created
        self.app.post("/register", data=test_user)

        # check if user exists in database
        with app.app_context():
            from src.utils.database import db
            sql = text("SELECT username FROM users")
            result = db.session.execute(sql).fetchone()
            if result:
                self.assertEqual(result[0], "test")
            else:
                raise AssertionError("No result from database")


    def test_register_no_password_confirmation(self):
        test_user = {
                "username": "test",
                "password1": "1234",
                }

        response = self.app.post("/register", data=test_user)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status, "400 BAD REQUEST")

    def test_register_empty_password_confirmation(self):
        test_user = {
                "username": "test",
                "password1": "1234",
                "password2": ""
                }

        response = self.app.post("/register", data=test_user)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'All fields not given' in response.data)

    def test_register_no_matching_password_confirmation(self):
        test_user = {
                "username": "test",
                "password1": "1234",
                "password2": "123"
                }

        response = self.app.post("/register", data=test_user)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Passwords don&#39;t match" in response.data) # url encoded '

    def test_register_duplicate_user(self):
        test_user = {
                "username": "test",
                "password1": "1234",
                "password2": "1234"
                }
        other_test_user = {
                "username": "test",
                "password1": "4321",
                "password2": "4321"
                }

        response = self.app.post("/register", data=test_user)
        response = self.app.post("/register", data=other_test_user)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Error in user creation' in response.data)

    # jos joskus PUT lisätään niin tämän testin voi vain poistaa
    def test_register_incorrect_method_put(self):
        test_user = {
                "username": "test",
                "password1": "1234",
                "password2": "1234"
                }
        response = self.app.put("/register", data=test_user)
        print(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertTrue(b'405 Method Not Allowed' in response.data)
