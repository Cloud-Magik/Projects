import csv
import getpass
import datetime
import random
import calendar
import psycopg2
import burner as b
user_id=0
l
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
                "\n\n\nWould you like to login to an existing account, register, or view account info? (Login/Register/View): ").upper()
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
                confirmed, user_id = b.Login(username, pass_word)
                if(confirmed):
                    break
            elif answer[:1].upper() == 'V':
                print("""\nPlease enter Login info""")
                username = input("Please enter username:").lower()
                pass_word = input("Please enter password:").lower()
                b.retrieveUsers(username, pass_word)
            else:
                print("Invalid entry")
                x = 1
        x = 1
        while True:

            answer = input(
                "\n\n\nWould you like to book a reservation, update a reservation, view a reservation, or cancel a reservation? (book/update/view/cancel): ").upper()
            if answer[:1].upper() == 'B':
                print("""\n Welcome to Paradise Falls, please book now!:
                """)
                arrival_date = input(
                    "choose arrival date *note numbersonly:")[:8]
                departure_date = input(
                    "choose departure date *note numbers only:")[:8]
                b.RoomTxt()
                room_package = input("choose room package:")
                b.Booking(arrival_date, departure_date, room_package, user_id)
                x = 1
            elif answer[:1].upper() == 'U':
                print("""\n  Update Reservation now!:
                      """)
                answer = input(
                    "\n\n\n What would you like to update? arrival date, departure date, or room package  (book/update/view): ").upper()
                if answer[:1].upper() == 'A':
                    arrival_date = input("choose arrival date:")
                elif answer[:1].upper() == 'D':
                    departure_date = input("choose departure date:")
                elif answer[:1].upper() == 'R':
                    room_package = input("choose room:")
                else:
                    print("Invalid entry")
                x = 1
            elif answer[:1].upper() == 'V':
                print("""\nPlease enter Confirmation Number
                """)
                confirmation_number = input("Enter Confirmation Number: ")
                confirmed = b.Confirmation(confirmation_number)
                if(confirmed):
                    break
            elif answer[:1].upper() == 'C':
                print("""\nPlease enter Confirmation Number
                """)
                confirmation_number = input("Enter Confirmation Number: ")
                confirmed = b.Confirmation(confirmation_number)
                if(confirmed):
                    break
            else:
                print("Invalid entry")
                x = 1

        x = 1
        while True:

            answer = input(
                "\n\n\nLets make your Payment(payment): ").upper()
            if answer[:1].upper() == 'P':
                first_name = input("Enter first name:").lower()
                last_name = input("Enter last name:").lower()
                credit_card_number = input("Enter credit card number:")
                expiration_date = input("Enter expiration date:")
                CCV = input("Enter CCV number:")
            else:
                print("Invalid entry")
                x = 1

    main()
except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
