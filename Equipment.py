from connection import *
from Associate import *

class Equipment:
    def __init__(self, no, amount, condition, branch):
        self.no = no
        self.amount = amount
        self.condition = condition
        self.branch = branch
        createEquipment(no, amount, condition, branch)
        
    def updateCondition(no, status):
        updateC(no, status)
        
    def addAmount(no):
        addEquipment(no)
    
    def getAmount(self):
        return self.amount
    
    def getCondition(self):
        return self.condition