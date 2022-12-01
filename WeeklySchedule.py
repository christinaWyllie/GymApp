from connection import *
from Employee import *
from Manager import *
from datetime import date

class WeeklySchedule:
    def __init__(self, manager):
        self.m_id = manager.getID()
        
        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday']
        today = date.today()
        self.week_no = today.isocalendar().week
        
    def changeWeek(self):
        self.week_no = self.week_no + 1
    
    def changeAvalability(self, rssn):
        return self.branch
    
    #def getSchedule()