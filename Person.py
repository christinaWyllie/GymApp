class Person:
    
    def __init__(self, ssn, f, l, address, phone, email):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        
    def removePerson(self, ssn):
        #do something with databse
        return self.ssn
        
    def getName(self):
        fullName = self.fname + self.lname
        return fullName
    
    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email
    
    def getSsn(self):
        return self.ssn
    
    def changeName(self,last):
        self.lname = last
        #need to update database
        
    def changePhone(self, phone):
        self.phone = phone
        #update database
        
    def changeEmail(self, email):
        self.email = email
        #update database