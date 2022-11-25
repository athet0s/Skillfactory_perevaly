import psycopg2


class DBManager:
    def __init__(self, name, host, login, password, port):
        self._name = name
        self._host = host
        self._login = login
        self._password = password
        self._port = port

    def __enter__(self):
        self._conn = psycopg2.connect(dbname=self._name, user=self._login,
                                      password=self._password, host=self._host, port=self._port)

        self._cursor = self._conn.cursor()
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
