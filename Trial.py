import csv

UserInfo=['ID','Email','Password', 'First Name','Last Name', '0']

with open ("Users.csv", 'a', newline='') as users:
    csvwriter = csv.writer(users) 
    csvwriter.writerow(UserInfo)


