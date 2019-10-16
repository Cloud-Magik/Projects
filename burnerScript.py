import csv
import datetime
import random
import calendar
import getpass
from burner import *
import psycopg2
try:
    conn = psycopg2.connect(
        database="project",
        user="postgres",
        password="0000",
        host="127.0.0.1",
        port="5432"
    )
# INTRO; Title page, Create user or login
# Paradisefalls()


# def main():

#     while True:

#         answer = input(
#             "\n\n\nWould you like to login to an existing account or register? (Login/Register): ")
#         if answer[:1].upper() == 'R':
#             register_user()

#         elif answer[:1].upper() == 'L':
#             log_in()
#             print("Succesful login!")
#             break
#         else:
#             print("Invalid entry")


# class User:
#     def __init__(self, username=None, password=None):
#         self.username = username
#         self.password = password


# def register_user():
#     print("\nLets register you")
#     user = User()
#     user.username = input("Enter Username to register: ").lower()
#     user.password = getpass.getpass("Enter your password: ")

#     csvfile = open('users.csv', 'a+')
#     csvfile.write(f"{user.username},{user.password}\n")
#     csvfile.close()


# def log_in():
#     print("Login info:")
#     username = input("Login with Username: ").lower()
#     password = getpass.getpass("Enter your password: ")

#     with open('users.csv') as csvfile:
#         CSVData = csv.reader(csvfile, delimiter=',')

#         userExists = False
#         for row in CSVData:

#             if username == row[0] and password == row[1]:

#                 userExists = True
#                 return True
#                 break

#         if not userExists:
#             print("User doesn't exist!")
#             log_in()
#     csvfile.close()


# main()
def insertNewUserInfo(email, first_name, last_name, username, pass_word):
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO User (email, first_name, last_name, username, pass_word) VALUES ('{email}','{first_name}', '{last_name}', '{username}', '{pass_word})"
    )
    conn.commit()
    print("Record inserted successfully")
    cursor.close()
    email = input("Please enter email to register:")
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    username = input("Enter username for account:")
    pass_word = input("Enter password for account:")

insertNewUserInfo(email, first_name, last_name, username, pass_word)
