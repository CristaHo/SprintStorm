import os
from unittest import TestCase, mock

from src.utils import config


class TestConfig(TestCase):
    @mock.patch.dict(os.environ, {"ENVIRONMENT": "test"}, clear=True)
    def test_env_when_set_as_not_production(self):
        curr_env = config.env()
        self.assertEqual(curr_env, "test")

    @mock.patch.dict(os.environ, {"ENVIRONMENT": "production"}, clear=True)
    def test_env_when_set_as_production(self):
        curr_env = config.env()
        self.assertEqual(curr_env, "production")

    @mock.patch.dict(os.environ, clear=True)
    def test_env_when_not_set(self):
        curr_env = config.env()
        self.assertEqual(curr_env, "production")

    @mock.patch.dict(os.environ, {"ENVIRONMENT": "hi"}, clear=True)
    def test_env_when_set_incorrectly(self):
        curr_env = config.env()
        self.assertEqual(curr_env, "production")


    @mock.patch.dict(os.environ, {"PORT": "5000"}, clear=True)
    def test_port_when_set_as_5000(self):
        curr_port = config.port()
        self.assertEqual(curr_port, 5000)

    @mock.patch.dict(os.environ, clear=True)
    def test_port_when_not_set(self):
        curr_port = config.port()
        self.assertEqual(curr_port, 3000)

    @mock.patch.dict(os.environ, {"PORT": "hi"}, clear=True)
    def test_port_when_set_incorrectly(self):
        curr_port = config.port()
        self.assertEqual(curr_port, 3000)


    @mock.patch.dict(os.environ, {"ENVIRONMENT": "production", "POSTGRES_URL": "postgresql://testurl"}, clear=True)
    def test_db_url_when_set_env_prod(self):
        curr_url = config.db_url()
        self.assertEqual(curr_url, "postgresql://testurl")

    @mock.patch.dict(os.environ, {"POSTGRES_URL": "postgresql://testurl", "TEST_POSTGRES_URL": "postgresql://othertest"}, clear=True)
    def test_db_url_when_set_env_not_set(self):
        curr_url = config.db_url()
        self.assertEqual(curr_url, "postgresql://testurl")

    @mock.patch.dict(os.environ, {"ENVIRONMENT": "test", "POSTGRES_URL": "postgresql://testurl", "TEST_POSTGRES_URL": "postgresql://othertest"}, clear=True)
    def test_db_url_when_env_not_prod(self):
        curr_url = config.db_url()
        self.assertEqual(curr_url, "postgresql://othertest")

    @mock.patch.dict(os.environ, clear=True)
    def test_db_url_when_db_not_set(self):
        self.assertRaises(RuntimeError, config.db_url)
