from connection import *
from Person import *

class Client(Person):
    
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.id = 8080990809809 #CHANGE THIS
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createClient(ssn, id, email, phone, f, l, address)
        
    def getClient(self):
        return self.ssn

    def addClient(self,person):
        id = 8888888888 #CHNAGE THIS 
        addNewClient(person.self.ssn, person.self.fname, person.self.lname, person.self.address,
                    person.self.phone, person.self.email, id)
        
    def removeC(self, ssn):
        removeClient(ssn)
    