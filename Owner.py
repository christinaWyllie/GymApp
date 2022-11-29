from connection import *
from Admin import *

class Owner(Admin):
    def __init__(self, ssn, email, phone, f, l, address,branch):
        self.ssn = ssn
        self.id =  868838383838383883
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = branch
        createOwner(ssn, id, email, phone, f, l, address, branch)
        
    def getowner(self):
        return self.ssn
        
  