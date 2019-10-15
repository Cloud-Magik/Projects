import psycopg2
try:
    conn = psycopg2.connect(
        database="project",
        user="postgres",
        password="0000",
        host="127.0.0.1",
        port="5432"
    )

    def createTables():
        cursor = conn.cursor()
        cursor.execute(
            """CREATE table users(
            user_id serial not null primary key,
            email text not null,
            first_name text not null,
            last_name text not null,
            username text not null,
            pass_word text not null
             )"""
        )
        conn.commit()

        cursor.execute(
            """CREATE table reservation(
                confirmation_number serial not null primary key,
                username text not null,
                arrival_date text not null,
                departure_date text not null,
                pass_word text not null
            )"""
        )
        conn.commit()

        cursor.close()
    createTables()
except (Exception, psycopg2.Error) as error:
    print("error while fetching data postgreSQL", error)
