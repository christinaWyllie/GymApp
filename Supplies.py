from connection import *

class Supplies:
    def __init__(self, branch, sname, supply, stock):
        self.branch_no = branch
        self.sname = sname
        self.supply_no = supply
        self.stock = stock
        createStock(branch, sname, supply, stock)
        
    def updateStock(branch, name, number, stock):
        updateS(branch, name, number, stock)
    
    def getStock(self):
        return self.stock
    
    def getName(self):
        return self.sname