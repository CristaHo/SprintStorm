from flask import Flask
from flask_testing import TestCase
from src.views.view_reference import view_reference_bp
from src.utils.database import db
from src.utils import config as conf

class AddReferenceTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.template_folder = '../src/templates'
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = conf.db_url() # Use a separate test database
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.register_blueprint(view_reference_bp)

        # Initialize SQLAlchemy with the app context
        db.init_app(app)

        return app

    def setUp(self):
        # Create the test database tables before each test
        db.create_all()

    def tearDown(self):
        # Drop the test database tables after each test
        db.session.remove()
        db.drop_all()

    def test_get_view_reference(self):
        response = self.client.get('/view_reference')
        self.assert_200(response)
