from connection import *
from Person import *

class Admin(Person):
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createAdmin(ssn, id, email, phone, f, l, address)
        self.id = getAdminID(ssn)
        
    def getAdmin(self):
        return self.ssn

    def addAdmin(self, person):
        self.id = getAdminID(self.person.ssn)
        addNewAdmin(self.person.ssn, self.person.fname, self.person.lname, self.person.address,
                    self.person.phone, self.person.email, self.id)
        
    def removeA(self, ssn):
        removeAdmin(ssn)