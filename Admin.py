from connection import *
from Person import *

class Admin(Person):
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.id =  868838383838383883
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createAdmin(ssn, id, email, phone, f, l, address)
        
    def getAdmin(self):
        return self.ssn

    def addAdmin(self, person):
        id = 8888888888 #CHNAGE THIS 
        addNewAdmin(person.self.ssn, person.self.fname, person.self.lname, person.self.address,
                    person.self.phone, person.self.email, id)
        
    def removeA(self, ssn):
        removeAdmin(ssn)