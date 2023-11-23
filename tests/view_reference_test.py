from flask import Flask
from flask_testing import TestCase
from src.views.view_reference import view_reference_bp

class AddReferenceTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__, template_folder='../src/templates')
        app.config["TESTING"] = True
        app.register_blueprint(view_reference_bp)
        return app

    def test_get_view_reference(self):
        response = self.client.get('/view_reference')
        self.assert_template_used('view_reference.html')
        self.assert_200(response)
