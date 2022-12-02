import mysql.connector
from mysql.connector import Error
from array import *

class Database:

    def __init__(self):
        self.connect = None
        self.cursor = None
        self.load()

    def load(self):
        self.connect = mysql.connector.connect(user = 'root', password = '30124336', 
                                            host = '127.0.0.1', database = 'gym_database')
        if self.connect.is_connected():
            self.cursor = self.connect.cursor()
        # except Error as e:
        #     print("Error occured while connecting.\n username, password or database name incorrect.\n")

    def close(self):
        self.connect.close()

# #create an new person in the Person table
    def createPerson(self, ssn, f, l, address, phone, email):
        insert = "INSERT INTO PERSON(ssn, fname, lname, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s)"
        values =(ssn, f, l, address, int(phone), email)
        self.cursor.execute(insert, values)
        self.connect.commit()
        
#     #delete an existing person
#     def deletePerson(ssn):
#         cursor.execute("DELETE FROM PERSON WHERE ssn = %s;", ssn)
#         connect.commit()
        
#     #update person's last name
#     def updatePersonName(ssn, lname):
#         cursor.execute("UPDATE PERSON SET lname = %s WHERE ssn = %s;", lname, ssn)
#         connect.commit()
        
#     #update person's phone number
#     def updatePersonPhone(ssn, phone):
#         cursor.execute("UPDATE PERSON SET phone_number = %s WHERE ssn = %s;", phone, ssn)
#         connect.commit()
        
#     #update person's email
#     def updatePersonEmail(ssn, email):
#         cursor.execute("UPDATE PERSON SET email = %s WHERE ssn = %s;", email, ssn)    
#         connect.commit()
        
#     #update person's address
#     def updatePersonAddress(ssn, address):
#         cursor.execute("UPDATE PERSON SET address = %s WHERE ssn = %s;", address, ssn)
#         connect.commit()
        
#     #create a client 
#     def createClient(ssn, id, email, phone, f, l, address):
#         cursor.execute("INSERT INTO CLIENT(cssn, client_id, fname, lname, address, phone_number, client_email)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
#         cursor.commit()
        
#     def addNewClient(self,ssn, fname, lname, address, phone, email, id):
#         cursor.execute("INSERT INTO CLIENT(cssn, client_id, fname, lname, address, phone_number, client_email)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, fname, lname, address, phone, email)
#         connect.commit()

#     #remove a client
#     def removeClient(ssn):
#         cursor.execute("DELETE FROM CLIENT WHERE ssn = %s;", ssn)
#         connect.commit()

#     def removeAdmin(ssn):
#         cursor.execute("DELETE FROM ADMIN WHERE ssn = %s;", ssn)
#         connect.commit()
        
#     def createAdmin(ssn, id, email, phone, f, l, address):
#         cursor.execute("INSERT INTO ADMIN(assn, admin_id, admin_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
#         connect.commit()
        
#     def addNewAdmin(self,ssn, fname, lname, address, phone, email, id):
#         cursor.execute("INSERT INTO ADMIN(assn, admin_id, admin_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, fname, lname, address, phone, email)
#         connect.commit()

#     def removeRUser(ssn):
#         cursor.execute("DELETE FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         connect.commit()
        
#     def createRUser(ssn, id, email, phone, f, l, address):
#         cursor.execute("INSERT INTO RESTRICTED_USER(assn, admin_id, admin_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
#         connect.commit()
        
#     def addNewUser(self,ssn, fname, lname, address, phone, email, id):
#         cursor.execute("INSERT INTO RESTRICTED_USER(rssn, r_user_id, r_user_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)",ssn, id, fname, lname, address, phone, email)
#         connect.commit()
        
#     def createEmployee(ssn, id, email, phone, f, l, address):
#         cursor.execute("INSERT INTO EMPLOYEE(essn, e_user_id, e_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
#         connect.commit()
        
#     def addNewEmployee(ssn, fname, lname, address, phone, email, id):
#         cursor.execute("INSERT INTO EMPLOYEE(essn, e_user_id, e_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s);", ssn, id, fname, lname, address, phone, email)
#         connect.commit()
        
#     def removeEmp(ssn):
#         cursor.execute("DELETE FROM EMPLOYEE WHERE ssn = %s;", ssn)
#         connect.commit()

#     def createOwner(ossn, owner_id, owner_email, Branch_num, f, l, address, phone_number):
#         cursor.execute("INSERT INTO OWNER(ossn, owner_id, owner_email, Branch_num, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", ossn, owner_id, owner_email, Branch_num, f, l, address, phone_number)
#         connect.commit()
        
#     def removeOwner(ossn):
#         cursor.execute("DELETE FROM OWNER WHERE ossn = %s;", ossn)
#         connect.commit()
        
#     def createAssociate(ssn, id, email, phone, f, l, address, branch):
#         cursor.execute("INSERT INTO ASSOCIATE(sssn, s_user_id, s_email, fname, lname, address, phone_number, branch_no)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s);",ssn, id, f, l, address, phone, email, branch)
#         connect.commit()
        
#     def deleteAssociate(ssn):
#         cursor.execute("DELETE FROM ASSOCIATE WHERE ssn = %s;", ssn)
#         connect.commit()
        
#     def createManager(mssn, m_id, m_email, branch_no, f, l, address, phone_number):
#         cursor.execute("INSERT INTO MANAGER(mssn, m_id, m_email, branch_no, f, l, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", mssn, m_id, m_email, branch_no, f, l, address, phone_number)
#         connect.commit()

#     def createTrainer(ssn, id, email, phone, f, l, address, branch):
#         cursor.execute("INSERT INTO TRAINER(tssn, t_user_id, t_email, fname, lname, address, phone_number, branch_no)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s);",ssn, id, f, l, address, phone, email, branch)
#         connect.commit()

#     def deleteTrainer(ssn):
#         cursor.execute("DELETE FROM TRAINER WHERE ssn = %s;", ssn)
#         connect.commit()

#     def addClassToTrainer(class_no, tssn):
#         cursor.execute("UPDATE TRAINER SET class_no = %s WHERE tssn = %s;", class_no, tssn)
#         connect.commit()

#     def createMember(mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number):
#         cursor.execute("INSERT INTO MEMBER(mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number)
#         connect.commit()

#     def updateMemberStatus(membership_id, status):
#         cursor.execute("UPDATE MEMBER SET status = %s WHERE membership_id = %s;", status, membership_id)
#         connect.commit()

#     def updateMemberType(membership_id, type):
#         cursor.execute("UPDATE MEMBER SET type = %s WHERE membership_id = %s;", type, membership_id)
#         connect.commit()

#     def updateScheduleAvail(day, r_user_id):
#         cursor.execute("UPDATE WEEKLY_SCHEDULE_AVAIL SET day = %s WHERE r_user_id = %s;", day,r_user_id)
#         connect.commit()

#     def createClass(class_no, date, time, branch_no, t_id, t_email, tssn):
#         cursor.execute("INSERT INTO CLASS(class_no, date, time, branch_no, t_id, t_email, tssn) VALUES(%s, %s, %s, %s, %s, %s, %s);", class_no, date, time, branch_no, t_id, t_email, tssn)
#         connect.commit()

#     def updateClassDate(date, class_no):
#         cursor.execute("UPDATE CLASS SET date = %s WHERE class_no = %s;", date, class_no)
#         connect.commit()

#     def updateClassTime(time, class_no):
#         cursor.execute("UPDATE CLASS SET time = %s WHERE class_no = %s;",time, class_no)
#         connect.commit()

#     def updateClassInstructor(tssn, t_id, t_email, class_no):
#         cursor.execute("UPDATE CLASS SET tssn = %s, t_id = %s, t_email = %s WHERE class_no = %s;", tssn, t_id, t_email, class_no)
#         connect.commit()

#     def createRoom(room_id, date, duration):
#         cursor.execute("INSERT INTO ROOM(room_id, date, duration) VALUES(%s, %s, %s);", room_id, date, duration)
#         connect.commit()

#     def cancelBooking(room_id, date, duration):
#         cursor.execute("DELETE FROM ROOMS WHERE room_id = %s, date = %s, duration = %s;",room_id, date, duration )
#         connect.commit()

#     def updateEquipCond(condition, equipment_no, branch_no):
#         cursor.execute("UPDATE EQUIPTMENT SET condition = %s WHERE equipment_no = %s AND branch_no = %s;", condition, equipment_no, branch_no)
#         connect.commit()

#     def createEquip(equipment_no, amount, condition, duration, branch_no):
#         cursor.execute("INSERT INTO EQUIPMENT(equipment_no, amount, condition, duration, branch_no) VALUES(%s, %s, %s, %s, %s);", equipment_no, amount, condition, duration, branch_no)
#         connect.commit()

#     def updateEquipAmount(amount, equipment_no, branch_no):
#         cursor.execute("UPDATE EQUIPMENT SET amount = %s WHERE equipment_no = %s AND branch_no = %s;", amount, equipment_no, branch_no)
#         connect.commit()

#     def createSupply(sname, supply_no, stock, branch_no):
#         cursor.execute("INSERT INTO SUPPLY(sname, supply_no, stock, branch_no) VALUES(%s, %s, %s, %s);", sname, supply_no, stock, branch_no)
#         connect.commit()

#     def updateSupplyStock(stock, supply_no, branch_no):
#         cursor.execute("UPDATE SUPPLIES SET stock = %s WHERE supply_no = %s AND branch_no = %s;", stock, supply_no, branch_no)
#         connect.commit()

#     def createGym(branch_no, location, o_ssn, mssn):
#         cursor.execute("INSERT INTO SUBSCRIPTION(branch_no, location, o_ssn, mssn) VALUES(%s, %s, %s, %s);", branch_no, location, o_ssn, mssn)
#         connect.commit()

#     #create new subscription
#     def createSubscription(login_id, name,status,branch_no):
#         cursor.execute("INSERT INTO SUBSCRIPTION(login_id, name, status, branch_no) VALUES (%s, %s, %s, %s);",login_id, name,status,branch_no)
#         connect.commit()

#     def updateSubscriptionStatus(status, login_id, branch_no):
#         cursor.execute("UPDATE SUBSCRIPTION SET status = %s WHERE login_id = %s AND branch_no = %s;", status, login_id, branch_no)
#         connect.commit()

#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()

#     def getManagerID(ssn):
#         cursor.execute("SELECT mssn FROM MANAGER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()

#     #https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
#     def getClasses():
#         cursor.execute("SELECT * FROM CLASS;")
#         data = cursor.fetchall()
#         classArray = []
#         for row in data:
#             new = []
#             for index in row:
#                 new.append(index)
                
#             classArray.append(new)
#         return classArray