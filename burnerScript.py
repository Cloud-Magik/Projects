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
    Paradisefalls()
    def main():
        while True:

            answer = input(
            "\n\n\nWould you like to login to an existing account or register? (Login/Register): ")
            if answer[:1].upper() == 'R':
                insertNewUser()

            elif answer[:1].upper() == 'L':
                Login()
                print("Succesful login!")
                break
            else:
                    print("Invalid entry")
    main()
except(Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)