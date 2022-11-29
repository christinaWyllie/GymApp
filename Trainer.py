from connection import *
from Employee import *
from Room import *

class Trainer(Employee):
    def __init__(self, ssn, email, phone, f, l, address, branch):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = branch
        createAssociate(ssn, id, email, phone, f, l, address, branch)
        self.id = getTrainerID(ssn)
        
    def __init__(self, ssn, email, phone, f, l, address, branch, classes):
        self.ssn = ssn
        self.id =  868838383838383883
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = branch
        self.classes = classes
        createAssociate(ssn, id, email, phone, f, l, address, branch)
        
    def getTrainer(self):
        return self.ssn
        
    def removeTrainer(self, ssn):
        deleteTrainer(ssn)
        
    def addClass(self, c):
        self.classes.append(c)
        
    def bookRoom(id, date, duration):
        return True