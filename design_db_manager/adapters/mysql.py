import pymysql.cursors


def connector(db: str, host='127.0.0.1', user='root', port=3306, **kwargs):
    return pymysql.connect(host=host,
                           port=port,
                           user=user,
                           db=db,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor,
                           **kwargs
                           )


def get_desc(user, database, **kwargs):
    # Query to get employees who joined in a period defined by two dates
    query = "show tables"
    conn = connector(db=database, user=user, **kwargs)
    try:
        with conn as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    finally:
        conn.close()


if __name__ == '__main__':
    get_desc("kiyama", "test_db", password="19980117")
