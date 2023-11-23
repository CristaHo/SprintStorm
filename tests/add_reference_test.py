from flask import Flask
from flask_testing import TestCase
from src.views.add_reference import add_reference_bp

class AddReferenceTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__, template_folder='../src/templates')
        app.config["TESTING"] = True
        app.register_blueprint(add_reference_bp)
        return app

    def test_get_add_reference(self):
        response = self.client.get('/add_reference')
        self.assert_template_used('add_reference.html')
        self.assert_200(response)

    def test_post_add_reference(self):
        data = {'author': 'Tester', 'title': 'Example Title', 'year': '2000'}
        response = self.client.post('/add_reference', data=data)
        
        self.assertIn(b'Tester', response.data)
        self.assertIn(b'Example', response.data)
        self.assertIn(b'2000', response.data)
        