from operation import operation
from hostel import Hostel
from genericUtils import Utils
from exceptions import NotEnoughHouseMates

class spend(operation):
    def __init__(self, command):
        if Hostel.memberList.__len__() < int(Utils.getParamValue('hostel', 'MIN_MEMBERS')):
            raise NotEnoughHouseMates("Minimum of " + Utils.getParamValue('hostel', 'MIN_MEMBERS') + \
                                    " needed to use expense calculator")
        else:
            super().__init__(command)

    def hasValidArguments(self):
        if len(self.operationArgs) < 3:
            return False
        else:
            if self.operationArgs[0].isdigit():
                for argument in self.operationArgs[1:]:
                    if not argument.isalpha():
                        return False
                    else:
                        return True
            else:
                return False

    def findLenders(self):
        lendersIndices = []
        nonlendersIndices = []
        allMemberIndices = [i for i in range(len(Hostel.memberList))]
        for idx, member in enumerate(Hostel.memberList):
            if Hostel.memberList[idx].totaldues < 0:
                Hostel.memberList[idx].isLender = True
                lendersIndices.append(idx)
            else:
                Hostel.memberList[idx].isLender = False
                nonlendersIndices.append(idx)
        return (lendersIndices, nonlendersIndices, allMemberIndices)

    def adjustDueOneLender(self, lendersIndices, nonlendersIndices, allMemberIndices):
        for idx, member in enumerate(Hostel.memberList):
            if idx in lendersIndices:           
                dictLenderDue = {}
                for idxNonlender in nonlendersIndices:
                    lenderName = Hostel.memberList[idxNonlender].name
                    dictLenderDue[lenderName] = 0
            else:
                dictLenderDue = {}
                for idxMember in allMemberIndices:
                    if idxMember != idx:
                        lenderName = Hostel.memberList[idxMember].name
                        if idxMember in lendersIndices:
                            dictLenderDue[lenderName] = Hostel.memberList[idx].totaldues
                        else:
                            dictLenderDue[lenderName] = 0
            Hostel.memberList[idx].dues = dictLenderDue

    def adjustDueMoreLender(self, lendersIndices, nonlendersIndices, allMemberIndices):
        for idx, member in enumerate(Hostel.memberList):
            if idx in nonlendersIndices:
                dictLenderDue = {}
                for idxLender in lendersIndices:
                    lenderName = Hostel.memberList[idxLender].name
                    dictLenderDue[lenderName] = Hostel.memberList[idxLender].totaldues * -1
            else:
                dictLenderDue = {}
                for idxMember in allMemberIndices:
                    if idxMember != idx:
                        memberName = Hostel.memberList[idxMember].name
                        dictLenderDue[memberName] = 0
            Hostel.memberList[idx].dues = dictLenderDue
        
    def adjustDue(self, forMembers):
        lendersIndices, nonlendersIndices, allMemberIndices = self.findLenders()

        if len(lendersIndices) == 2: 
            self.adjustDueMoreLender(lendersIndices, nonlendersIndices, allMemberIndices)

        if len(lendersIndices) == 1: 
            self.adjustDueOneLender(lendersIndices, nonlendersIndices, allMemberIndices)
        

    def do(self):
        status = None

        spentAmount = int(self.operationArgs[0])

        forMembers = self.operationArgs[2:]
        byMember = self.operationArgs[1]
        idxByMember = Hostel.searchMember(byMember)

        avgDue = round(spentAmount / (len(forMembers)+1) )

        for forMember in forMembers:
            idxForMember = Hostel.searchMember(forMember)
            if idxForMember == -1:
                status = 'MEMBER_NOT_FOUND'
            else:
                Hostel.memberList[idxByMember].totaldues -= avgDue 
                Hostel.memberList[idxForMember].totaldues += avgDue
                status = 'SUCCESS'

        self.adjustDue(forMembers)

        return status
