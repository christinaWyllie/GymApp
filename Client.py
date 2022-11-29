from connection import *
from Person import *

class Client(Person):
    
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createClient(ssn, id, email, phone, f, l, address)
        self.id = getClientID(ssn)
        
    def getClient(self):
        return self.ssn

    def addClient(self,person):
        self.id = getClientID(self.person.ssn)
        addNewClient(self.person.ssn, self.person.fname, self.person.lname, self.person.address,
                    self.person.phone, self.person.email, self.id)
        
    def removeC(self, ssn):
        removeClient(ssn)
    