from connection import *
from RestrictedUser import *

class Employee(RestrictedUser):
    
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createEmployee(ssn, id, email, phone, f, l, address)
        self.id = getEmployeeID(ssn)
        
    def getEmployee(self):
        return self.ssn

    def addEmployee(self, person):
        self.id = getEmployeeID(ssn)
        addNewEmployee(self.person.ssn, self.person.fname, self.person.lname, self.person.address,
                    self.person.phone, self.person.email, self.id)
        
    def removeEmployee(self, ssn):
        removeEmp(ssn)