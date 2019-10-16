import psycopg2
try:
    conn = psycopg2.connect(
        database="project",
        user="postgres",
        password="0000",
        host="127.0.0.1",
        port="5432"
    )
# **********INSERT FUNCTIONS... Functions for how we will make contact with database**********

# login info inserted into postgreSQL database

    # def insertUser():
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         """INSERT INTO users ( email, first_name, last_name, username, pass_word)
    #         VALUES (agoodfella@Live.com', 'Daniel', 'Morales', '', '')"""
    #     )
    #     conn.commit()
    #     cursor.close()
    # insertUser()

    # Reservation info inserted into postgreSQL database

    def insertReservation():
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO reservation (arrival_date, departure_date, room_package, price)
            VALUES ('','', 'Hollywood Suite', '$159.99')"""
        )
        conn.commit()
        cursor.close()
    insertReservation()
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
