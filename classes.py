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
    def __init__(self, data):
        self._data = data

    def insert_data(self):
        user_id = self.insert_or_update_user()
        coord_id = self.insert_coords()
        pereval_id = self.insert_pereval(user_id, coord_id)
        self._conn.commit()
        return pereval_id

    def insert_or_update_user(self):
        user = self._data.user
        self._cursor.execute('''INSERT INTO users (fam, name, otc, phone, email) 
                                  VALUES (%s, %s, %s, %s, %s) 
                                  ON CONFLICT(email) DO UPDATE SET
                                  (fam, name, otc, phone) = (EXCLUDED.fam, EXCLUDED.name, EXCLUDED.otc, EXCLUDED.phone)
                                  RETURNING id;
                              ''',
                             (user.fam, user.name, user.otc, user.phone, user.mail))
        pk = self._cursor.fetchone()[0]
        return pk

    def insert_coords(self):
        coords = self._data.coords
        self._cursor.execute("INSERT INTO coords (latitude, longitude, height) VALUES (%s, %s, %s,) RETURNING id",
                             (float(coords.latitude), float(coords.longitude), int(coords.height)))
        pk = self._cursor.fetchone()[0]
        return pk

    def insert_pereval(self, user_id, coord_id):
        data = self._data
        level = data.level
        self._cursor.execute('''INSERT INTO pereval_added (beauty_title, title, other_titles, connect, add_time,
                                    level_winter, level_summer, level_autumn, level_spring, user_id, coord_id) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                                    RETURNING id;
                             ''',
                             (data.beauty_title, data.title, data.other_titles, data.connect, data.add_time,
                              level.winter, level.summer, level.autumn, level.spring, user_id, coord_id))

        pk = self._cursor.fetchone()[0]
        return pk
