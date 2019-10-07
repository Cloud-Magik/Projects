from collections import namedtuple
import datetime
import random
import calendar

Reservation = namedtuple(
    'Reservation', 'room arr_date dept_date guest_name confirmation_num')

#Variables and Lists

confirmation_counter = 0
bedroom_selections = []
reservations_list = []

#INTRO; Title page, Create user or login