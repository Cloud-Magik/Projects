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
            user_id serial primary key,
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
                confirmation_number serial primary key,
                user_id integer,
                arrival_date text not null,
                departure_date text not null,
                constraint foreign key (user_id) references users (user_id)
            )"""
        )
        conn.commit()

        #select * from users as u 
        #inner join reservation as r on r.user_id=ur.user_id
        cursor.close()
    createTables()
except (Exception, psycopg2.Error) as error:
    print("error while fetching data postgreSQL", error)
