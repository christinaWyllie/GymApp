from connection import *

class Subscription:
    def __init__(self, login, name, branch):
        self.login = login
        self.name = name
        self.status = True
        self.branch_no = branch
        createSubscription(login, name, self.status, branch)
        
    def getStatus(self):
        return self.status
    
    def setStatus(self, stat):
        self.status = stat
        updateSubscriptionStatus(self.status, self.login, self.branch_no)