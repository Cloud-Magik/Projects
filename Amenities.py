import pprint
print("We have the following amenities with Wifi and complimentary breakfast to all rooms :")


Amenities = {
    "1.Spa treatment--massage and skin treatment": "$25",
    "2.Unlimited mini fridge access": "$15",
    "3.Open bar throughout lounges in hotel": "$30",
    "4.Golf course access": "$40",
    "5.Entertainment room and theatre privileges": "$10",
    "6.Water park tickets": "$45",
    "7.Snorkeling tour": "$50",
    "8.B&H Sailing": "$100"
}
pprint.pprint(Amenities)

############################################################################
# AMENITIES AS CLASS
# class Reservation:
#        def __init__(self,passenger_id,passenger_fname,passenger_lname):
#       self.passenger_id = passenger_id
#       self.passenger_fname = passenger_fname
#       self.passenger_lname = passenger_lname
#       self.cost = 0
#       self.reservation_id = []
#       self.passenger_record = {'p_name'  : self.passenger_fname + self.passenger_lname,
#                              'p_id'    : self.passenger_id,
#                              'p_wallet': self.cost,
#                              'p_reservation_id': self.reservation_id,
#                             }
#       self.airline_seats = { 'Business Class' : 50,
#                            'First Class'    : 50,
#                            'Premium Economy': 100,
#                            'Regular Economy': 150 }
#       self.airline_price = { 'Business Class' : 2500,
#                            'First Class'    : 2000,
#                            'Premium Economy': 1800,
#                            'Regular Economy': 1500 }
#       self.hotel_room = {'Penthouse'             : 10,
#                        'King Deluxe Bedroom'    : 20,
#                        'Queen Deluxe Bedroom'   : 20,
#                        'Kind Standard Bedroom' : 30,
#                        'Queen Standard Bedroom': 50 }
#       self.hotel_price = {'Penthouse'            : 1000,
#                         'King Deluxe Bedroom'    : 700,
#                         'Queen Deluxe Bedroom'   : 600,
#                         'Kind Standard Bedroom' : 450,
#                         'Queen Standard Bedroom': 350 }
#    def currentStatus(self,option):
#        if option == "Airline":
#            for key, value in self.airline_seats.items():
#               print key, value
#        elif option == "Hotel":
#            for key,value in self.hotel_room.items():
#               print key, value

#    def Total(self):
#        print self.passenger_record['p_wallet']

# class Airline(Reservation):
#    def __init__(self,passenger_id,passenger_fname,passenger_lname,airline_seat_section,
#          airline_departure_date):
#        Reservation.__init__(self,passenger_id,passenger_fname,passenger_lname)
#        self.airline_seat_section = airline_seat_section
#        self.airline_departure_date = airline_departure_date

#    def CheckAvailability(self):
#        if  (self.airline_seats.get(self.airline_seat_section) != 0):
#             self.airline_seats[self.airline_seat_section] -= 1
#             self.passenger_record['p_wallet'] +=        self.airline_price[self.airline_seat_section]
#             print "\n\nReserved Airline Ticket\n\n"

# class Hotel(Reservation):
#     def __init__(self,passenger_id,passenger_fname,passenger_lname,hotel_room_selection,
#              hotel_check_in_date,hotel_check_out_date):
#         Reservation.__init__(self,passenger_id,passenger_fname,passenger_lname)
#         self.hotel_room_selection = hotel_room_selection
#         self.hotel_check_in_date = hotel_check_in_date
#         self.hotel_check_out_date = hotel_check_out_date

#     def CheckAvailability(self):
#         if (self.hotel_room.get(self.hotel_room_selection) != 0):
#             self.hotel_room[self.hotel_room_selection] -= 1
#             self.passenger_record['p_wallet'] += self.hotel_price[self.hotel_room_selection]
#             print "\n\nReserved Hotel Room\n\n"

# A1 = Airline("1","Arun","Raman","Business Class","07-07-2014")
# A1.CheckAvailability()
# A1.currentStatus("Airline")
# H1 = Hotel("1","Arun","Raman","Penthouse","07-07-2014","07-10-2014")
# H1.CheckAvailability()
# H1.currentStatus("Hotel")