from collections import namedtuple
import datetime
import random
import calendar

#---------------------------------------------------------------
# Requirements for project
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
#---------------------------------------------------------------


Reservation = namedtuple(
    'Reservation', 'room arr_date dept_date guest_name confirmation_num')

#Variables and Lists

confirmation_counter = 0
bedroom_selections = []
reservations_list = []

# INTRO; Title page, Create user or login

x = open("Title.txt", "r")
print(x.read())