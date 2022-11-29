from connection import *
from Admin import *

class Owner(Admin):
    def __init__(self, ssn, email, phone, f, l, address,branch):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = branch
        createOwner(ssn, id, email, phone, f, l, address, branch)
        self.id = getOwnerID(ssn)
        
    def getowner(self):
        return self.ssn
    
    def removeOwn(ossn):
        removeOwner(ossn)
        
  