from unittest import TestCase
from sqlalchemy import text
from flask import session
from src.app import app

class TestLoginView(TestCase):
    def setUp(self):
        test_user = {
                "username": "test",
                "password1": "12345678",
                "password2": "12345678"
                }
        self.app = app.test_client()
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

        response = self.app.post("/register", data=test_user)
        self.assertEqual(response.status_code, 302)

    def test_login_page_is_shown(self):
        response = self.app.get("/login")
        self.assertTrue(b'Username:' in response.data)
        self.assertTrue(b'Password:' in response.data)
        self.assertTrue(b'Login' in response.data)

    def test_existing_user_can_login(self):
        test_user = {
                "username": "test",
                "password": "12345678"
                }
        response = self.app.post("/login", data=test_user)
        self.assertEqual(response.status_code, 302) # redirect
        with self.app.session_transaction() as s:
            self.assertEqual(s["uid"], 1)

    def test_correct_userid_set_to_session(self):
        other_test_user = {
                "username": "othertest",
                "password1": "43215678",
                "password2": "43215678"
                }
        other_user_login = {
                "username": "othertest",
                "password": "43215678",
                }
        self.app.post("/register", data=other_test_user)
        response = self.app.post("/login", data=other_user_login)
        self.assertEqual(response.status_code, 302) # redirect
        with self.app.session_transaction() as s:
            self.assertEqual(s["uid"], 2)

    def test_incorrect_username_cant_login(self):
        test_user = {
                "username": "somewrongname",
                "password": "12345678"
                }
        response = self.app.post("/login", data=test_user)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Invalid username or password' in response.data)

        with self.app.session_transaction() as s:
            self.assertEqual(s.get("uid"), None)

    def test_incorrect_password_cant_login(self):
        test_user = {
                "username": "test",
                "password": "12354678"
                }
        response = self.app.post("/login", data=test_user)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Invalid username or password' in response.data)

        with self.app.session_transaction() as s:
            self.assertEqual(s.get("uid"), None)
