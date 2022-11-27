from connection import *
from Person import *

def __init__(self, ssn, id, email, phone, f, l, address):
    self.ssn = ssn
    self.id = id
    self.fname = f
    self.lname = l
    self.address = address
    self.phone = phone
    self.email = email
    createClient(ssn, id, email, phone, f, l, address)
    
def getClient(self):
    return self.ssn

def addClient(person):
    