import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#from Config import config


# def connect():

#     conn = None
#     try:
#         params = config()
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)

#         cur = conn.cursor()
try:
    conn = psycopg2.connect(
        database="Cohort2",
        user="postgres",
        password="6108",
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
    # def retrieveUserInfo(id):
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         f"SELECT first_name, last_name, phone_number FROM cohort2 WHERE user_id={id}"
    #     )
    #     rows = cursor.fetchall()
    #     if(rows):
    #         for row in rows:
    #             print(f'''
    #            First Name: {row[0]}
    #            Last Name: {row[1]}
    #            Phone: {row[2]}
    #            ''')
    #             cursor.close()
    #     else:
    #         print("Your database is empty")
    # userId = int(input("Enter the customer's id to pull their info >> "))
    # retrieveUserInfo(userId)
except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)


#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')

#         db_version=cur.fetchone()
#         print(db_version)
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as Error:
#         print(Error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')

# if __name__== '__main__':
#     connect()
