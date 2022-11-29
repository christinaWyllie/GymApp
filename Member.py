from connection import *
from Client import *

class Member(Client):
    def __init__(self, ssn, email, phone, f, l, address, memberID, type, status):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.memberID = memberID
        self.type = type
        self.status = status
        createMember(ssn, id, email, phone, f, l, address,memberID, type, status)
        self.id = getMemberID(ssn)
        
    def getType(self, memberID):
        return self.type
        
    def getStatus(self, memberID):
        return self.status
        
    def changeStatus(self, memberID, stat):
        self.status = stat
        updateStatus(memberID, stat)
        
    def setType(self, id, type):
        self.type = type
        updateType(id, type)