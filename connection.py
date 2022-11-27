import mysql.connector
from mysql.connector import Error

try:
    connect = mysql.connector.connect(user = 'final', password = 'cpsc', 
                                        host = '127.0.0.1', database = 'gym_database')
    if connect.is_connected():
        cursor = connect.cursor()
        
        
except Error as e:
    print("Error occured while connecting.\n username, password or database name incorrect.\n")

#create an new person in the Person table
def createPerson(ssn, f, l, address, phone, email):
    cursor.execute("INSERT INTO PERSON(ssn, fname, lname, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s);",
                   ssn, f, l, address, phone, email)
    
    connect.commit()
    
#delete an existing person
def deletePerson(ssn):
    cursor.execute("DELETE FROM PERSON WHERE ssn = %s;", ssn)
    connect.commit()
    
#update person's last name
def updatePersonName(ssn, lname):
    cursor.execute("UPDATE PERSON SET lname = %s WHERE ssn = %s;", lname, ssn)
    connect.commit()
    
#update person's phone number
def updatePersonPhone(ssn, phone):
    cursor.execute("UPDATE PERSON SET phone_number = %s WHERE ssn = %s;", phone, ssn)
    connect.commit()
    
#update person's email
def updatePersonEmail(ssn, email):
    cursor.execute("UODATE PERSON SET email = %s WHERE ssn = %s;", email, ssn)    
    connect.commit()
    
#update person's address
def updatePersonAddress(ssn, address):
    cursor.execute("UPDATE PERSON SET address = %s WHERE ssn = %s;", address, ssn)
    connect.commit()
    
    
    
    
connect.close()