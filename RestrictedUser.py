from connection import *
from Person import *

class RestrictedUser(Person):
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.id =  868838383838383883
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createRUser(ssn, id, email, phone, f, l, address)
        
    def getRUser(self):
        return self.ssn

    def addRUser(self, person):
        id = 8888888888 #CHNAGE THIS 
        addNewUser(person.self.ssn, person.self.fname, person.self.lname, person.self.address,
                    person.self.phone, person.self.email, id)
        
    def removeRU(self, ssn):
        removeRUser(ssn)