from itertools import chain
from typing import Optional, List

import pymysql.cursors


class MySQLManager:
    def __init__(self, db: str, host: str = '127.0.0.1', port: int = 3306, user: str = 'root',
                 password: Optional[str] = None, charset: str = 'utf8mb4'):
        self.db = db
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset

    def _connector(self, **kwargs):
        return pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               charset=self.charset,
                               # cursorclass=pymysql.cursors.DictCursor,
                               **kwargs
                               )

    def get_tables(self) -> iter:
        """

        Returns:
            iter: iterable of table names

        """
        # Query to get employees who joined in a period defined by two dates
        query = "show tables"
        conn = self._connector()
        try:
            with conn as cursor:
                cursor.execute(query)
                tables_data = cursor.fetchall()
                return chain.from_iterable(tables_data)
        finally:
            conn.close()


if __name__ == '__main__':
    print(list(MySQLManager("test_db", user="kiyama", password="19980117").get_tables()))
    # print(MySQLManager("test_db", user="kiyama", password="19980117").get_tables())
