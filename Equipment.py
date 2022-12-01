from connection import *
from Associate import *

class Equipment:
    def __init__(self, no, amount, condition, branch):
        self.no = no
        self.amount = amount
        self.condition = condition
        self.branch = branch
        createEquip(no, amount, condition, branch)
        
    def updateCondition(self, status):
        updateEquipCond(self.no, status)
        self.status = status
        
    def addAmount(self):
        updateEquipAmount(self.no)
        self.amount = self.amount +1
    
    def getAmount(self):
        return self.amount
    
    def getCondition(self):
        return self.condition