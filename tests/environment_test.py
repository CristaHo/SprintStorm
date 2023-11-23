from unittest import TestCase, mock
from src.utils.environment import read_postgres_url

class TestEnvironment(TestCase):
    @mock.patch.dict("os.environ", {"ENVIRONMENT": "production", "POSTGRES_URL": "postgresql://jadajadajadajaa"})
    def test_read_postgres_url_production(self):
        url = read_postgres_url()
        self.assertIsNotNone(url)
        self.assertIn("postgresql://", url)

    @mock.patch.dict("os.environ", {"ENVIRONMENT": "development", "TEST_POSTGRES_URL": "postgresql://jadajadajadajaa"})
    def test_read_postgres_url_development(self):
        url = read_postgres_url()
        self.assertIsNotNone(url)
        self.assertIn("postgresql://", url)

    @mock.patch.dict("os.environ", {"TEST_POSTGRES_URL": "postgresql://jadajadajadajaa"}, clear=True)
    def test_read_postgres_url_no_environment(self):
        url = read_postgres_url()
        self.assertIsNotNone(url)
        self.assertIn("postgresql://", url)

    @mock.patch.dict("os.environ", {}, clear=True)
    def test_read_postgres_url_no_environment_no_url(self):
        url = read_postgres_url()
        self.assertIsNone(url)

    @mock.patch.dict("os.environ", {"ENVIRONMENT": "production", "TEST_POSTGRES_URL": "postgresql://jadajadajadajaa"}, clear=True)
    def test_read_postgres_url_wrong_url_production(self):
        url = read_postgres_url()
        self.assertIsNone(url)

    @mock.patch.dict("os.environ", {"ENVIRONMENT": "development", "POSTGRES_URL": "postgresql://jadajadajadajaa"}, clear=True)
    def test_read_postgres_url_wrong_url_development(self):
        url = read_postgres_url()
        self.assertIsNone(url)

    @mock.patch.dict("os.environ", {"ENVIRONMENT": "production"}, clear=True)
    def test_read_postgres_url_no_url_production(self):
        url = read_postgres_url()
        self.assertIsNone(url)

    @mock.patch.dict("os.environ", {"ENVIRONMENT": "development"}, clear=True)
    def test_read_postgres_url_no_url_development(self):
        url = read_postgres_url()
        self.assertIsNone(url)