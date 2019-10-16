import csv
import datetime
import random
import calendar
import getpass

# ---------------------------------------------------------------
# ******************Requirements for project********************
# fill brackets with [X] when requirements are fulfilled
# use comments [X]
# exceptions for inputs; make the code unbreakable []
# save info and pull information from database []
# calculations clean []
# CRUD operations (create,read,update,delete)[]
# use classes []
# use objects[]
# use loops[]
# use arrays[]
# use Lists[]
# use conditionals[]
# use functions[]
# use file imports[]
# use discounts or incentive for project[]
# ---------------------------------------------------------------

# INTRO; Title page, Create user or login


def Paradisefalls():
    Title = open("Title.txt")
    print(Title.read())
    Title.close()


Paradisefalls()


def main():

    while True:

        answer = input(
            "\n\n\nWould you like to login to an existing account or register? (Login/Register): ")
        if answer[:1].upper() == 'R':
            register_user()

        elif answer[:1].upper() == 'L':
            log_in()
            print("Succesful login!")
            break
        else:
            print("Invalid entry")


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


def register_user():
    print("\nLets register you")
    user = User()
    user.username = input("Enter Username to register: ").lower()
    user.password = getpass.getpass("Enter your password: ")

    csvfile = open('users.csv', 'a+')
    csvfile.write(f"{user.username},{user.password}\n")
    csvfile.close()


def log_in():
    print("Login info:")
    username = input("Login with Username: ").lower()
    password = getpass.getpass("Enter your password: ")

    with open('users.csv') as csvfile:
        CSVData = csv.reader(csvfile, delimiter=',')

        userExists = False
        for row in CSVData:

            if username == row[0] and password == row[1]:

                userExists = True
                return True
                break

        if not userExists:
            print("User doesn't exist!")
            log_in()
    csvfile.close()


main()
