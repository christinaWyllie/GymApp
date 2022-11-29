from connection import *
from Subscription import *
from Employee import *
from Class import *
from Owner import *
from Manager import *

class Gym:
    def __init__(self, branch, loc, ssn, email, id):
        self.branch_no = branch
        self.location = loc
        manager = Manager(ssn, email, id)