import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="0000",
        host="127.0.0.1",
        port="5432"
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    def createDB():
        cursor = conn.cursor()
        cursor.execute(
            sql.SQL("CREATE DATABASE {}").format(sql.Identifier('Hotel'))
        )

        cursor.close()

    createDB()
    
except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

