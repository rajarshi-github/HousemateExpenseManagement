
from genericUtils import Utils
from readInputs import readInputs
from members import Member
from hostel import Hostel


def operationToClassMapping(command):
    ops = Utils.getParamValue('operations', 'operation').split(',')
    cls = Utils.getParamValue('operations', 'classname').split(',')

    return dict(zip(ops, cls))[command]



class operation():
    def __init__(self, command):
        self.operationType = command[0]
        self.operationArgs = command[1].split()

    def isValid(self):
        if self.operationType in Utils.getParamValue('operations', 'operation'):
            return True
        else:
            return False

    def hasValidArguments(self, n):
        if len(self.operationArgs) != n:
            return False
        else:
            return True

    def __call__(self):
        return 'Calling ' + str(self.__class__) + ' , type : ' + self.operationType + \
                 ', arguments : ' + ' '.join(self.operationArgs)
        

class moveIn(operation):
    def __init__(self, command):
        super().__init__(command)

    def hasValidArguments(self):
        return super().hasValidArguments( n=1)

    def do(self):
        memberNameToAdd = self.operationArgs[0]
        return Hostel.addMember ( newMember= Member(name=memberNameToAdd) )
        #print(doStatus)
        

class moveOut(operation):
    def __init__(self, command):
        super().__init__(command)

    def hasValidArguments(self):
        return super().hasValidArguments( n=1)

    def do(self):
        memberName = self.operationArgs[0]
        return Hostel.removeMember (memberName) 


class spend(operation):
    def __init__(self, command):
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

    def adjustDue(self, forMembers):

        # find lenders
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

        if len(lendersIndices) == 2: 

            for idx, member in enumerate(Hostel.memberList):
                if idx in nonlendersIndices:
                    dictLenderDue = {}
                    for idxLender in lendersIndices:
                        lenderName = Hostel.memberList[idxLender].name
                        dictLenderDue[lenderName] = Hostel.memberList[idxLender].totaldues * -1

                    #Hostel.memberList[idx].dues = dictLenderDue
                else:
                    dictLenderDue = {}
                    for idxMember in allMemberIndices:
                        if idxMember != idx:
                            memberName = Hostel.memberList[idxMember].name
                            dictLenderDue[memberName] = 0

                Hostel.memberList[idx].dues = dictLenderDue


        if len(lendersIndices) == 1: 

            for idx, member in enumerate(Hostel.memberList):
                if idx in lendersIndices:           
                    dictLenderDue = {}
                    for idxNonlender in nonlendersIndices:
                        lenderName = Hostel.memberList[idxNonlender].name
                        dictLenderDue[lenderName] = 0

                    #Hostel.memberList[idx].dues = dictLenderDue
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
        #print('Before adjustment ... ')
        #Hostel.getMembers()
        self.adjustDue(forMembers)
        #print('After adjustment ... ')
        #Hostel.getMembers()

        return status

class getDues(operation):
    def __init__(self, command):
        super().__init__(command)

    def hasValidArguments(self):
        return super().hasValidArguments( n=1)

    def do(self):
        memberName = self.operationArgs[0]
        dueDict = Hostel.getDuesOfMember ( memberName=memberName ) 

        dueDict = dict(sorted(dueDict.items(), key=lambda item: item[1], reverse=True))
        dueDict = dict(sorted(dueDict.items()))

        for name, due in dueDict.items():
            print(name, due) 
        


class clearDues(operation):
    def __init__(self, command):
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










