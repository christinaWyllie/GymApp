from connection import *
from Employee import *

class Associate(Employee):
    def __init__(self, ssn, email, phone, f, l, address, branch):
        self.ssn = ssn
        self.id =  868838383838383883
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = branch
        createAssociate(ssn, id, email, phone, f, l, address, branch)
        
    def getAssociate(self):
        return self.ssn
        
    def removeAssociate(self, ssn):
        deleteAssociate(ssn)
        
    def setEquipment(self, Equipment e):
        self.equipment = e