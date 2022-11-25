import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class DBManager:
    DB_NAME = os.getenv("FSTR_DB_NAME")
    DB_HOST = os.getenv("FSTR_DB_HOST")
    DB_LOGIN = os.getenv("FSTR_DB_LOGIN")
    DB_PASS = os.getenv("FSTR_DB_PASS")
    DB_PORT = os.getenv("FSTR_DB_PORT")

    def __enter__(self):
        self._conn = psycopg2.connect(dbname=DBManager.DB_NAME, user=DBManager.DB_LOGIN,
                                      password=DBManager.DB_PASS, host=DBManager.DB_HOST, port=DBManager.DB_PORT)

        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._cursor.close()
        self._conn.close()


class PerevalManager(DBManager):
    def insert_data(self, data):
        self.insert_or_update_user(data.user)
        self.insert_coords(data.coords)
        self.insert_level(data.level)
        self.insert_pereval(data.beauty_title, data.title, data.other_titles, data.connect, data.add_time)

    def insert_or_update_user(self, user):
        pass

    def insert_coords(self, coords):
        pass

    def insert_level(self, level):
        pass

    def insert_pereval(self, beauty_title, title, other_titles, connect, add_time):
        pass
