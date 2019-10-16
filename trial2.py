import psycopg2
try:
   conn = psycopg2.connect(
       database="Cohort2",
       user="postgres",
       password="6108",
       host="127.0.0.1",
       port="5432"
   )
   def retrieveUserInfo(id): #Display info option
       cursor = conn.cursor()
       cursor.execute(
           f"SELECT first_name, last_name, phone_number FROM cohort2 WHERE user_id={id}"
       )
       rows = cursor.fetchall()
       if(rows):
           for row in rows:
               print(f'''
              First Name: {row[0]}
              Last Name: {row[1]}
              Phone: {row[2]}
              ''')
               cursor.close()
       else:
           print("Your database is empty")
   userId = int(input("Enter the customer's id to pull their info >> "))
   retrieveUserInfo(userId)
   def insertUserInfo(name, lname, phone): #registration
       cursor = conn.cursor()
       cursor.execute(
           f"INSERT INTO cohort2 (first_name, last_name, phone_number) VALUES ('{name}', '{lname}', '{phone}')"
       )
       conn.commit()
       print("record inserted successfully")
       cursor.close()
   name = input("enter name >>")
   lname = input("enter last name >>")
   phone = input("enter phone number >> ")
   insertUserInfo(name, lname, phone)
   def deleteUserInfo(id): #delete 
       cursor = conn.cursor()
       cursor.execute(
           f"DELETE FROM cohort2 WHERE user_id={id}"
       )
       print("record deleted successfully")
       cursor.close()
   userId = int(input("enter the customer's id you want to delete >> "))
   deleteUserInfo(userId)
   def updateUserInfo(column_name, newValue, id): #update info
       cursor = conn.cursor()
       cursor.execute(
           f"UPDATE cohort2 SET {column_name}='{newValue}' WHERE user_id={id}"
       )
       conn.commit()
       cursor.close()
       print("record updated successfully")
   id = int(input("enter your id >>"))
   selection = int(input('''what do you want to update
   1.First Name
   2.Last Name
   3.Phone Number)
   make a selection [1-3] >> '''))
   newValue = input("enter new value >>")
   if(selection == 1):
       updateUserInfo("first_name", newValue, id)
   elif (selection == 2):
       updateUserInfo("last_name", newValue, id)
   else:
       updateUserInfo("phone_number", newValue, id)
   def retrieveAllUsers():
       cursor = conn.cursor()
       cursor.execute(
           f"SELECT * FROM cohort2"
       )
       rows = cursor.fetchall()
       if(rows):
           for row in rows:
               print('''
               ID: {0}
               First Name: {1}
               Last Name: {2}
               Phone: {3}
               '''.format(row[0], row[1], row[2], row[3]))
       else:
           print("Your database is empty")
       cursor.close()
   retrieveAllUsers()
except(Exception, psycopg2.Error) as error:
   print("Error while fetching data from PostgreSQL", error)