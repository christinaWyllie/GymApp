from connection import *

class Class:
    def __init__(self, no, date, time, branch, ssn, id, email):
        self.class_no = no
        self.date = date
        self.time = time
        self.branch_no = branch
        self.tssn = ssn
        self.t_id = id
        self.t_email = email
        createClass(no, date, time, branch, ssn, id, email)
        
    def getDate(self):
        return self.date
    
    def setDate(self, date):
        self.date = date
        changeDate(date, self.class_no, self.branch)
        
    def changeTime(self, time):
        self.time = time
        changeTime_Class(time, self.class_no, self.date, self.branch)
        
    def changeInstructor(self, ssn, id, email):
        self.tssn = ssn
        self.t_id = id
        self.t_email = email
        changeInstructor_Class(ssn, id, email, self.class_no)