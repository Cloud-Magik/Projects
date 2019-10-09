import csv
email = []
password = []
guestname =[]

with open('users.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
