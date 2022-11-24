import psycopg2


class DBManager:
    def __init__(self, name, host, login, password, port):
        self._conn = psycopg2.connect(dbname=name, user=login,
                                      password=password, host=host, port=port)

        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._cursor.close()
        self._conn.close()

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()

    def query(self, sql):
        self._cursor.execute(sql)
        return self.fetchall()
