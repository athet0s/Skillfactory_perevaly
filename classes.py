import os
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv
from datetime import datetime
from schemas import Pereval
from sql import *

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

        self._cursor = self._conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._cursor.close()
        self._conn.close()


class PerevalManager(DBManager):

    def insert_data(self, data: Pereval):
        user_id = self._insert_or_update_user(data)
        coord_id = self._insert_coords(data)
        pereval_id = self._insert_pereval(data, user_id, coord_id)
        self._insert_images(data, pereval_id)
        self._conn.commit()
        return pereval_id

    def _insert_or_update_user(self, data: Pereval):
        user = data.user
        self._cursor.execute(SQL_INSERT_OR_UPDATE_USERS,
                             ({'fam': user.fam,
                               'name': user.name,
                               'otc': user.otc,
                              'phone': user.phone,
                               'email': user.email}))
        pk = self._cursor.fetchone()[0]
        return pk

    def _insert_coords(self, data: Pereval):
        coords = data.coords
        self._cursor.execute(SQL_INSERT_COORDS,
                             ({'latitude': float(coords.latitude),
                               'longitude': float(coords.longitude),
                               'height': int(coords.height)}))
        pk = self._cursor.fetchone()[0]
        return pk

    def _insert_pereval(self, data: Pereval, user_id: int, coord_id: int):
        level = data.level
        self._cursor.execute(SQL_INSERT_PEREVAL,
                             ({'beauty_title': data.beauty_title,
                               'title': data.title,
                               'other_titles': data.other_titles,
                               'connect': data.connect,
                               'add_time': data.add_time,
                               'level_winter': level.winter,
                               'level_summer': level.summer,
                               'level_autumn': level.autumn,
                               'level_spring': level.spring,
                               'user_id': user_id,
                               'coord_id': coord_id,
                               'status': 'new',
                               'date_added': datetime.now()}))

        pk = self._cursor.fetchone()[0]
        return pk

    def _insert_images(self, data, pereval_id: int):
        for i in data.images:
            self._cursor.execute(SQL_INSERT_PEREVAL_IMAGES,
                                 ({'title': i.title,
                                   'img': i.data,
                                   'date_added': datetime.now()}))
            image_id = self._cursor.fetchone()[0]
            self._cursor.execute(SQL_INSERT_PEREVAL_ADDED_PEREVAL_IMAGES,
                                 ({'pereval_id': pereval_id,
                                   'image_id': image_id}))

    def get_pereval_data_by_id(self, pereval_id: int):
        self._cursor.execute(SQL_SELECT_PEREVAL_BY_ID, (pereval_id,))
        pereval = self._cursor.fetchone()
        if not pereval:
            return False
        return dict(pereval)

    def get_perevals_by_user_email(self, user_email: str):
        self._cursor.execute(SQL_SELECT_PEREVALS_BY_USER_EMAIL, (user_email,))
        perevals = self._cursor.fetchall()
        if len(perevals) == 0:
            return False
        return [dict(pereval) for pereval in perevals]

    def update_data(self, pereval_id: int, data: Pereval):
        self.validate_pereval_update_id_and_email(pereval_id, data.user.email)
        self._update_pereval(pereval_id, data)
        self._update_coords(pereval_id, data)
        self._conn.commit()
        return True

    def _update_pereval(self, pereval_id: int, data: Pereval):
        level = data.level
        self._cursor.execute(SQL_UPDATE_PEREVAL, ({'id': pereval_id,
                                                   'beauty_title': data.beauty_title,
                                                   'title': data.title,
                                                   'other_titles': data.other_titles,
                                                   'connect': data.connect,
                                                   'level_winter': level.winter,
                                                   'level_summer': level.summer,
                                                   'level_autumn': level.autumn,
                                                   'level_spring': level.spring}))
        print(self._cursor.rowcount)

    def _update_coords(self, pereval_id: int, data: Pereval):
        coords = data.coords
        self._cursor.execute(SQL_UPDATE_COORDS, ({'latitude': float(coords.latitude),
                                                  'longitude': float(coords.longitude),
                                                  'height': int(coords.height),
                                                  'pereval_id': pereval_id}))

    def is_pereval_exists(self, pereval_id: int):
        self._cursor.execute(SQL_IS_PERVAL_ID_EXISTS, (pereval_id,))
        return self._cursor.fetchone()[0]

    def is_email_exists(self, email: str):
        self._cursor.execute(SQL_IS_USER_EMAIL_EXISTS, (email,))
        return self._cursor.fetchone()[0]

    def is_pereval_poster_email_matches_user_email(self, pereval_id: int, email: str):
        self._cursor.execute(SQL_SELECT_USER_EMAIL_BY_PEREVAL_ID, (pereval_id,))
        return self._cursor.fetchone()[0] == email

    def validate_pereval_update_id_and_email(self, pereval_id: int, email: str):
        if not self.is_pereval_exists(pereval_id):
            raise PerevalUpdateExeption(0)
        if not self.is_email_exists(email):
            raise PerevalUpdateExeption(1)
        if not self.is_pereval_poster_email_matches_user_email(pereval_id, email):
            raise PerevalUpdateExeption(2)
        return True


class PerevalUpdateExeption(Exception):

    def __init__(self, error_code):
        self.error_code = error_code

