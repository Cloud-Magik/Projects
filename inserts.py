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

# New user registration info inserted into postgreSQL database

    # def insertNewUser(email, first_name, last_name, username, pass_word):
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         f"INSERT INTO User (email, first_name, last_name, username, pass_word) VALUES ('{email}','{first_name}', '{last_name}', '{username}', '{pass_word})"
    #     )
    #     conn.commit()
    #     print("Record inserted successfully")
    #     cursor.close()
    #     email = input("Please enter email to register:")
    #     first_name = input("Enter first name:")
    #     last_name = input("Enter last name:")
    #     username = input("Enter username for account:")
    #     pass_word = input("Enter password for account:")

    #     insertNewUser(email, first_name, last_name, username, pass_word)

# Login Authentication where checks if you have account in postgreSQL database

    def Login(username, pass_word):
        print("""****** PLEASE LOG IN ******
        """)
        username = input("Username: ")
        pass_word = input("Password: ")
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM users WHERE username='{username}' AND pass_word='{pass_word}'")
        rows = cursor.fetchall()
        if(rows):
            print("You have succesfully logged in!")
        else:
            print("Wrong credentials")
        cursor.close()
# Reservation info inserted into postgreSQL database

    def insertReservation(arrival_date, departure_date, room_package):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO reservation (arrival_date, departure_date, room_package) VALUES ('{arrival_date}','{departure_date}', '{room_package}')"
        )
        conn.commit()
        print("Record inserted successfully")
        cursor.close()
        # email = input("Please enter email to register:")--reservartion is going to need other half of function to avoid breaking
        # first_name = input("Enter first name:")
        # last_name = input("Enter last name:")
        # username = input("Enter username for account:")
        # pass_word = input("Enter password for account:")

        insertNewUser(email, first_name, last_name, username, pass_word)   
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
