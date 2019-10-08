import csv
filename = users.csv
fields = ['ID','email','password','firstname','lastname','confirmationnumber']
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.appen(row)
print('field names are:' + ','.join(field for field in fields))