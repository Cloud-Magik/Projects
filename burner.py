import getpass
import psycopg2

try:
    conn = psycopg2.connect(
        database="project",
        user="postgres",
        password="0000",
        host="127.0.0.1",
        port="5432"
    )

    def Paradisefalls():
        Title = open("Title.txt")
        print(Title.read())
        Title.close()

    def RoomTxt():
        Rooms = open("RoomTxt.txt")
        print(Rooms.read())

    def test():
        print('test')

    def insertNewUser(email, first_name, last_name, username, pass_word):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO users (email, first_name, last_name, username, pass_word) VALUES ('{email}','{first_name}', '{last_name}', '{username}', '{pass_word}')"
        )
        conn.commit()
        cursor.execute(
            f"SELECT user_id FROM users WHERE username='{username}' AND pass_word='{pass_word}'")
        rows = cursor.fetchall()
        if (rows):
            
            for row in rows:
                user_id = row[0]
                print("Record inserted successfully")
                print(f"Your UserID is:{user_id}")
        cursor.close()

    def retrieveUsers():
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT user_id, email, first_name, last_name, username, pass_word FROM users WHERE username = {username} AND pass_word={pass_word}"
        )
        rows = cursor.fetchone()
        if(rows):
            for row in rows:
                print('''
                User ID: {0}
                email: {1}
                First Name: {2}
                Last Name: {3}
                username: {4
                pass_word: {5}}
                '''.format(row[0], row[1], row[2], row[3], row[4], row[5]))
        else:
            print("Your database is empty")
        cursor.close()
    retrieveUsers()

    def Login(username, pass_word):
        isWrongConfirmed = False
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM users WHERE username='{username}' AND pass_word='{pass_word}'")
        rows = cursor.fetchall()
        if(rows):
            isWrongConfirmed = True
            for row in rows:
                user_id = row[0]
                print("You have succesfully logged in!")
                print(f"""Your userID is :{user_id}""")

        else:
            print("Wrong credentials")
            isWrongConfirmed = False
        return isWrongConfirmed

        cursor.close()

    def Booking(arrival_date, departure_date, room_package):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO reservation (arrival_date, departure_date, room_package) VALUES ('{arrival_date}', '{departure_date}', '{room_package}')"
            )
        cursor.execute(
            f"SELECT user_id FROM users WHERE username='{username}' AND pass_word='{pass_word}'")
        rows = cursor.fetchall()
        conn.commit()
        print("Record inserted successfully")
        cursor.close()

    def cancel(confirmation_number):
        cursor = conn.cursor()
        cursor.execute(
            f"DELETE * FROM reservation WHERE confirmation_number='{confirmation_number}'")
        cursor.commit()
        print("record deleted successfully")
        cursor.close()
except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
