import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pilots_certificates")

mycursor = mydb.cursor()


def create_pilot_id():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    mycursor.execute(
        f"INSERT INTO pilots (first_name, last_name) VALUES ('{firstName}', '{lastName}')")


def create_certificates():
    pilotID = int(input("Enter pilotID:"))
    name = input("Enter certificate name: ")
    issue = input("Enter issue date [YYYY-MM-DD]: ")
    expiration = input("Enter expiration date [YYYY-MM-DD]: ")
    mycursor.execute(
        f"INSERT INTO certificates (name, issue_date, expiration_date, pilot_id) VALUES ('{name}', '{issue}', '{expiration}', {pilotID})")


def read_certificates():
    pilotID = int(input("Enter pilotID:"))
    mycursor.execute(f"SELECT * FROM certificates WHERE pilot_id={pilotID}")
    result = mycursor.fetchall()

    # loop through the rows
    for row in result:
        print(row, '\n')


def delete_certificates():
    pilotID = int(input("Enter pilotID:"))
    my_value = input("Enter certificate name to delete: ")
    mycursor.execute(f"DELETE FROM certificates WHERE name='{my_value}' AND pilot_id={pilotID}")


def update_certificates():
    pilotID = int(input("Enter Pilot ID to update certificate: "))
    name = input("Enter name to update: ")
    issue = input("Enter issue date to update: ")
    expiration = input("Enter expiration date to update: ")
    mycursor.execute(
        f"UPDATE certificates SET name = '{name}', issue_date= '{issue}', expiration_date='{expiration}' WHERE pilot_id = {pilotID};")


def start_application():
    """Gets the inputs from pilots"""

    print("Welcome to pilot certificates tracker")
    selection = ""

    while not selection == 'q':
        print("\nSelect an option: ")
        print("Create a certificate [c]: ")
        print("Read a certificate [r]: ")
        print("update a certificate [u]: ")
        print("Delete a certificate [d]: ")
        selection = input("Enter your selection [q to quit]: ")
        
        if selection == 'c':
                create_certificates()
                mydb.commit()
        
        elif selection == 'r':
                read_certificates()

        elif selection == 'u':
                update_certificates()
                mydb.commit()

        elif selection == 'd':
                delete_certificates()
                mydb.commit()

        else:
                return
        

start_application()

