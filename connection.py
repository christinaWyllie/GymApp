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
    cursor.execute("INSERT INTO PERSON(ssn, fname, lname, address, phone_number, email)\
        VALUES (%s, %s, %s, %s, %s, %s);", ssn, f, l, address, phone, email)
    
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
    cursor.execute("UPDATE PERSON SET email = %s WHERE ssn = %s;", email, ssn)    
    connect.commit()
    
#update person's address
def updatePersonAddress(ssn, address):
    cursor.execute("UPDATE PERSON SET address = %s WHERE ssn = %s;", address, ssn)
    connect.commit()
    
    
def createClient(ssn, id, email, phone, f, l, address):
    cursor.execute("INSERT INTO CLIENT(cssn, client_id, fname, lname, address, phone_number, client_email)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
    cursor.commit()
    
def addNewClient(self,ssn, fname, lname, address, phone, email, id):
    cursor.execute("INSERT INTO CLIENT(cssn, client_id, fname, lname, address, phone_number, client_email)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, fname, lname, address, phone, email)
    cursor.commit()

def removeClient(ssn):
    cursor.execute("DELETE FROM CLIENT WHERE ssn = %s;", ssn)
    cursor.commit()

def removeAdmin(ssn):
    cursor.execute("DELETE FROM ADMIN WHERE ssn = %s;", ssn)
    cursor.commit()
    
def createAdmin(ssn, id, email, phone, f, l, address):
    cursor.execute("INSERT INTO ADMIN(assn, admin_id, admin_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
    cursor.commit()
    
def addNewAdmin(self,ssn, fname, lname, address, phone, email, id):
    cursor.execute("INSERT INTO ADMIN(assn, admin_id, admin_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, fname, lname, address, phone, email)
    cursor.commit()

def removeRUser(ssn):
    cursor.execute("DELETE FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
    cursor.commit()
    
def createRUser(ssn, id, email, phone, f, l, address):
    cursor.execute("INSERT INTO RESTRICTED_USER(assn, admin_id, admin_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
    cursor.commit()
    
def addNewUser(self,ssn, fname, lname, address, phone, email, id):
    cursor.execute("INSERT INTO RESTRICTED_USER(rssn, r_user_id, r_user_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)",ssn, id, fname, lname, address, phone, email)
    cursor.commit()
    
def createEmployee(ssn, id, email, phone, f, l, address):
    cursor.execute("INSERT INTO EMPLOYEE(essn, e_user_id, e_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
    cursor.commit()
    
def addNewEmployee(ssn, fname, lname, address, phone, email, id):
    cursor.execute("INSERT INTO EMPLOYEE(essn, e_user_id, e_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s);", ssn, id, fname, lname, address, phone, email)
    cursor.commit()
    
def removeEmp(ssn):
    cursor.execute("DELETE FROM EMPLOYEE WHERE ssn = %s;", ssn)
    cursor.commit()
    
def createAssociate(ssn, id, email, phone, f, l, address, branch):
    cursor.execute("INSERT INTO ASSOCIATE(sssn, s_user_id, s_email, fname, lname, address, phone_number, branch_no)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);",ssn, id, f, l, address, phone, email, branch)
    cursor.commit()
    
def deleteAssociate(ssn):
    cursor.execute("DELETE FROM ASSOCIATE WHERE ssn = %s;", ssn)
    cursor.commit()
    
    
def createTrainer(ssn, id, email, phone, f, l, address, branch):
    cursor.execute("INSERT INTO TRAINER(tssn, t_user_id, t_email, fname, lname, address, phone_number, branch_no)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);",ssn, id, f, l, address, phone, email, branch)
    cursor.commit()

def deleteTrainer(ssn):
    cursor.execute("DELETE FROM TRAINER WHERE ssn = %s;", ssn)
    cursor.commit()

def addClassToTrainer(class_no, tssn):
    cursor.execute("UPDATE TRAINER SET class_no = %s WHERE tssn = %s;", class_no, tssn)
    cursor.commit()

def updateScheduleAvail(day, r_user_id):
    cursor.execute("UPDATE WEEKLY_SCHEDULE_AVAIL SET day = %s WHERE r_user_id = %s;", day,r_user_id)
    connect.commit()

def createClass(class_no, date, time, branch_no, t_id, t_email, tssn):
    cursor.execute("INSERT INTO CLASS(class_no, date, time, branch_no, t_id, t_email, tssn) VALUES(%s, %s, %s, %s, %s, %s, %s);", class_no, date, time, branch_no, t_id, t_email, tssn)
    connect.commit()

def updateClassDate(date, class_no):
    cursor.execute("UPDATE CLASS SET date = %s WHERE class_no = %s;", date, class_no)
    connect.commit()

def updateClassTime(time, class_no):
    cursor.execute("UPDATE CLASS SET time = %s WHERE class_no = %s;",time, class_no)
    connect.commit()

def updateClassInstructor(tssn, t_id, t_email, class_no):
    cursor.execute("UPDATE CLASS SET tssn = %s, t_id = %s, t_email = %s WHERE class_no = %s;", tssn, t_id, t_email, class_no)
    connect.commit()

def createRoom(room_id, date, duration):
    cursor.execute("INSERT INTO ROOM(room_id, date, duration) VALUES(%s, %s, %s);", room_id, date, duration)
    connect.commit()

def cancelBooking(room_id, date, duration):
    cursor.execute("DELETE FROM ROOMS WHERE room_id = %s, date = %s, duration = %s;",room_id, date, duration )
    connect.commit()

def updateEquipCond(condition, equipment_no, branch_no):
    cursor.execute("UPDATE EQUIPTMENT SET condition = %s WHERE equipment_no = %s AND branch_no = %s;", condition, equipment_no, branch_no)
    connect.commit()

def createEquip(equipment_no, amount, condition, duration, branch_no):
    cursor.execute("INSERT INTO EQUIPMENT(equipment_no, amount, condition, duration, branch_no) VALUES(%s, %s, %s, %s, %s);", equipment_no, amount, condition, duration, branch_no)
    connect.commit()
#create new subscription
def createSubscription(login_id, name,status,branch_no):
    cursor.execute("INSERT INTO SUBSCRIPTION(login_id, name, status, branch_no) VALUES (%s, %s, %s, %s);",login_id, name,status,branch_no)
    connect.commit()

def updateSubscriptionStatus(status, login_id, branch_no):
    cursor.execute("UPDATE SUBSCRIPTION SET status = %s WHERE login_id = %s AND branch_no = %s;", status, login_id, branch_no)
    connect.commit()


connect.close()