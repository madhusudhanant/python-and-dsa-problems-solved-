import pymysql
def get_connection():
    c = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'yuvasakthi'
    )
    return c