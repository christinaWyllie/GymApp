from connection import *
from RestrictedUser import *

class Employee(RestrictedUser):
    
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.id =  868838383838383883
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createEmployee(ssn, id, email, phone, f, l, address)
        
    def getEmployee(self):
        return self.ssn

    def addEmployee(self, person):
        id = 8888888888 #CHNAGE THIS 
        addNewEmployee(person.self.ssn, person.self.fname, person.self.lname, person.self.address,
                    person.self.phone, person.self.email, id)
        
    def removeEmployee(self, ssn):
        removeEmp(ssn)