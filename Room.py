from connection import *

class Room:
    def __init__(self, id, date, duration):
        self.id = id
        self.date = date
        self.duration = duration
        createBooking(id, date, duration)
        
    def booked(id, date, duration):
        canBook = isBooked()
        if(canBook == True):
            book(id, date, duration)
        #else:
            #print message here
    
    def cancelBooking(id, date, duration):
        cancelB(id, date, duration)