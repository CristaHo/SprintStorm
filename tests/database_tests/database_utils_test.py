from unittest import TestCase

from src.app import app
from sqlalchemy import text

class TestDatabaseUtils(TestCase):
    def table_exists(self, table_name):
        sql = text("SELECT EXISTS (SELECT FROM pg_tables WHERE tablename = :tablename)")
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(sql, {"tablename": table_name}).fetchone()
        if result:
            return result[0]
        else:
            raise AssertionError("Database didn't return anything")

    # tests if the tables exist or not
    def all_tables_exist(self, exist: bool=True):
        is_article = self.table_exists("article")
        is_book = self.table_exists("book")
        is_reference = self.table_exists("reference")
        is_category = self.table_exists("category")
        self.assertEqual(is_article, exist)
        self.assertEqual(is_book, exist)
        self.assertEqual(is_reference, exist)
        self.assertEqual(is_category, exist)

    def test_all_tables_exist(self):
        self.all_tables_exist()

    def test_drop_tables_sql_drops_all_tables(self):
        with app.app_context():
            from src.utils.database import drop_tables
            drop_tables()
        self.all_tables_exist(False)

    def test_schema_sql_creates_tables(self):
        with app.app_context():
            from src.utils.database import init_tables, drop_tables
            drop_tables()
            init_tables()
        self.all_tables_exist(True)
