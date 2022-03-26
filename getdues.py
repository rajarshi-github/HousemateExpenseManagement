from operation import operation
from hostel import Hostel
from exceptions import NotEnoughHouseMates
from genericUtils import Utils

class getDues(operation):
    def __init__(self, command):
        if Hostel.memberList.__len__() < int(Utils.getParamValue('hostel', 'MIN_MEMBERS')):
            raise NotEnoughHouseMates("Minimum of " + Utils.getParamValue('hostel', 'MIN_MEMBERS') + \
                                    " needed to use expense calculator")
        else:
            super().__init__(command)

    def hasValidArguments(self):
        return super().hasValidArguments( n=1)

    def do(self):
        memberName = self.operationArgs[0]
        dueDict = Hostel.getDuesOfMember ( memberName=memberName ) 
        if dueDict == 'MEMBER_NOT_FOUND':
            print('MEMBER_NOT_FOUND')
        else:
            dueDict = dict(sorted(dueDict.items(), key=lambda item: (-item[1], item[0] )))

            for name, due in dueDict.items():
                print(name, due) 
            
