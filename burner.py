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

    def test():
        print('test')

    def insertNewUser(email, first_name, last_name, username, pass_word):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO users (email, first_name, last_name, username, pass_word) VALUES ('{email}','{first_name}', '{last_name}', '{username}', '{pass_word}')"
        )
        conn.commit()
        print("Record inserted successfully")
        cursor.close()

    def Login(username, pass_word):
        isWrongConfirmed = False
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM users WHERE username='{username}' AND pass_word='{pass_word}'")
        rows = cursor.fetchall()
        if(rows):
            print("You have succesfully logged in!")
            isWrongConfirmed = True
        else:
            print("Wrong credentials")
            isWrongConfirmed = False
        return isWrongConfirmed

        cursor.close()
except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
