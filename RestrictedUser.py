from connection import *
from Person import *

class RestrictedUser(Person):
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createRUser(ssn, id, email, phone, f, l, address)
        self.id = getRUserID(ssn)
        
    def getRUser(self):
        return self.ssn

    def addRUser(self, person):
        self.id = getRUserID(ssn)
        addNewUser(self.person.ssn, self.person.fname, self.person.lname, self.person.address,
                    self.person.phone, self.person.email, self.id)
        
    def removeRU(self, ssn):
        removeRUser(ssn)