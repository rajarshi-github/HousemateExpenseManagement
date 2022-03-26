from operation import operation
from hostel import Hostel
from genericUtils import Utils
from exceptions import NotEnoughHouseMates

class clearDues(operation):
    def __init__(self, command):
        if Hostel.memberList.__len__() < int(Utils.getParamValue('hostel', 'MIN_MEMBERS')):
            raise NotEnoughHouseMates("Minimum of " + \
                                    Utils.getParamValue('hostel', 'MIN_MEMBERS') + \
                                    " needed to use expense calculator")
        else:
            super().__init__(command)

    def hasValidArguments(self):
        if super().hasValidArguments( n=3):
            if not self.operationArgs[2].isdigit():
                return False
            else:
                if self.operationArgs[0].isalpha() and self.operationArgs[1].isalpha():
                    return True
                else:
                    return False
        else:
            return False

    def do(self):
        byMember = self.operationArgs[0]
        forMember = self.operationArgs[1]
        dueClearingAmount = int(self.operationArgs[2])

        idxByMember = Hostel.searchMember( memberName= byMember)
        if idxByMember != -1:
            if forMember in Hostel.memberList[idxByMember].dues.keys():
                if dueClearingAmount <= Hostel.memberList[idxByMember].dues[forMember]:

                    Hostel.memberList[idxByMember].dues[forMember] -= dueClearingAmount
                    Hostel.memberList[idxByMember].totaldues -= dueClearingAmount 

                    idxForMember = Hostel.searchMember(memberName=forMember)

                    Hostel.memberList[idxForMember].totaldues += dueClearingAmount

                    return Hostel.memberList[idxByMember].dues[forMember] 
                else:
                    return 'INCORRECT_PAYMENT'
            else:
                return 'LENDER_NOT_FOUND'
        else:
            return 'MEMBER_NOT_FOUND' 
