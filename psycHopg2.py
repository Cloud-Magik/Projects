import psycopg2

try:
    conn = psycopg2.connect(
        database="Cohort2",
        user="postgres",
        password="6108",
        host="127.0.0.1",
        port="5432"
    )

    def retrieveUserInfo(email):
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT email, pass_word, first_name, last_name, confirmation_number FROM Cohort2 WHERE email={email}"
        )
        rows = cursor.fetchall()
        if(rows):
            for row in rows:
                print(f'''
                email: {row[0]}
                password: {row[1]}
                first name: {row[2]}
                last name: {row[3]}
                confirmation number: {row[4]}
                ''')
                cursor.close
            else:
                print("Your database is empty")
    email =str(input("Enter the customer's email to pull their info: "))
    retrieveUserInfo(email)

    def insertUserInfo(email, password, fname, lname, cnum):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO Cohort2 (email, pass_word, first_name, last_name) VALUES ('{email}','{password}', '{firstname}', '{lastname}')"
        )
        con.commit()
        print("Record inserted successfully")
        cursor.close()
    email=input("Enter email: ")
    password=input("Enter password: ")
    firstname=input("Enter first name: ")
    lastname=input("Enter last name: ")