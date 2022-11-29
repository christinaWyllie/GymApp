from connection import *

class Class:
    def __init__(self, login, name, branch):
        self.login = login
        self.name = name
        self.status = True
        self.branch_no = branch
        createSub(login, name, branch)
        
    def getStatus(self):
        return self.status
    
    def setStatus(self, stat):
        self.status = stat
        changeStatus(stat, self.branch, self.name)