import psycopg2
try:
    # CONNECTION...
    conn = psycopg2.connect(
        database="Hotel",
        user="postgres",
        password="0000",
        host="127.0.0.1",
        port="5432"
    )

    # AUTHENTICATION....
    def createTables():
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE users (
            user_id SERIAL NOT NULL PRIMARY KEY,
            email TEXT NOT NULL, 
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL, 
            username TEXT NOT NULL,
            pass_word TEXT NOT NULL,
            ---- maybe foreign key to change tables
            )"""
        )
        conn.commit()

    # RESERVATION...
        cursor.execute(
            """CREATE TABLE users (
            confirmation_number SERIAL NOT NULL PRIMARY KEY,
            username TEXT NOT NULL,
            arrival_date TEXT NOT NULL,    -- change to dates
            departure_date TEXT NOT NULL, --change to dates
            pass_word TEXT NOT NULL,
            )"""
        )
        conn.commit()

        cursor.close()
    createTables()
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)
