import psycopg2
try:
   conn = psycopg2.connect(
       database="Cohort2",
       user="postgres",
       password="6108",
       host="127.0.0.1",
       port="5432"
   )
   def retrieveUserInfo(id):
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
   userId=int(input("Enter the customer's id to pull their info >> "))
   retrieveUserInfo(userId)
except(Exception, psycopg2.Error) as error:
   print("Error while fetching data from PostgreSQL", error)