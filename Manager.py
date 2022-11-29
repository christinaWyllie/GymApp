from connection import *
from Admin import *

class Manager(Admin):
    def __init__(self, ssn, email, phone, f, l, address,branch):
        self.ssn = ssn
        self.id =  86883838383
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = branch
        createManager(ssn, id, email, phone, f, l, address, branch)
        
    def getManager(self):
        return self.ssn
    
    def getID(self):
        return self.id
    
    def getBranch(self):
        return self.branch