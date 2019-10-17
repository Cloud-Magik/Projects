import getpass
import psycopg2
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
print("""\nPlease enter registration info for Paradise Falls
    """)

def Login(username, pass_word):
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM users WHERE username='{username}' AND pass_word='{pass_word}'")
    rows = cursor.fetchall()
    if(rows):
        print("You have succesfully logged in!")
    else:
        print("Wrong credentials")
    cursor.close()

