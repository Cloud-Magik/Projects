import csv
import getpass
import datetime
import random
import calendar
import psycopg2
import burner as b

try:
    conn = psycopg2.connect(
        database="project",
        user="postgres",
        password="0000",
        host="127.0.0.1",
        port="5432"
    )
    b.Paradisefalls()

    def main():
        x = 1
        while True:

            answer = input(
                "\n\n\nWould you like to login to an existing account or register? (Login/Register): ").upper()
            if answer[:1].upper() == 'R':
                print("""\nPlease enter registration info for Paradise Falls
    """)
                email = input("Please enter email to register:").lower()
                first_name = input("Enter first name:").lower()
                last_name = input("Enter last name:").lower()
                username = input("Enter username for account:").lower()
                pass_word = getpass.getpass(
                    "Enter password for account:").lower()
                b.insertNewUser(email, first_name, last_name,
                                username, pass_word)
                x = 1
            elif answer[:1].upper() == 'L':
                print("""\nPlease enter Login info
                """)
                username = input("Username: ").lower()
                pass_word = getpass.getpass("Password: ").lower()
                confirmed = b.Login(username, pass_word)
                if(confirmed):
                    break
            else:
                print("Invalid entry")
                x = 1
        
    main()
except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
