from itertools import chain
from typing import Optional

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

    def _connector(self, is_dict: bool = True, **kwargs):
        if is_dict:
            cursor_class = pymysql.cursors.DictCursor
        else:
            cursor_class = pymysql.cursors.Cursor
        return pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               charset=self.charset,
                               cursorclass=cursor_class,
                               **kwargs
                               )

    def execute(self, query: str, args=None, is_dict=True):
        conn = self._connector(is_dict)
        try:
            with conn as cursor:
                cursor.execute(query, args)
                return cursor.fetchall()
        finally:
            conn.close()

    def table_names(self) -> iter:
        """

        Returns:
            iter: iterable of table names

        """
        # Query to get employees who joined in a period defined by two dates
        query = "show tables"
        tables_data = self.execute(query, is_dict=False)
        return chain.from_iterable(tables_data)

    def field_data(self, table_name: str):
        """

        Returns:
            iter: iterable of table:data

        """
        query = "show full columns from {}".format(table_name)
        # query = "show full columns from product"
        tables_data = self.execute(query)
        return tables_data


if __name__ == '__main__':
    mm = MySQLManager("test_db", user="kiyama", password="19980117")
    x: str
    for x in mm.table_names():
        print(x)
        y = mm.field_data(x)
        print(y)
