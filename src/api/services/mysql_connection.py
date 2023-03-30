from mysql.connector import connect

from src.constants import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USER


def get_mysql_connection():
    db  = connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
    return db 