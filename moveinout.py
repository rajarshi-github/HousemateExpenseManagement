from operation import operation
from hostel import Hostel
from members import Member
from exceptions import NotEnoughHouseMates
from genericUtils import Utils

class moveIn(operation):
    def __init__(self, command):
        super().__init__(command)

    def hasValidArguments(self):
        return super().hasValidArguments( n=1)

    def do(self):
        memberNameToAdd = self.operationArgs[0]
        return Hostel.addMember ( newMember= Member(name=memberNameToAdd) )        

class moveOut(operation):
    def __init__(self, command):
        super().__init__(command)

    def hasValidArguments(self):
        return super().hasValidArguments( n=1)

    def do(self):
        memberName = self.operationArgs[0]
        return Hostel.removeMember (memberName) 
