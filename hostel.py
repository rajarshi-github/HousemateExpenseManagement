from genericUtils import Utils


class Hostel():

    memberList = []

    @classmethod
    def addMember(self, newMember):
        if len(Hostel.memberList) < int(Utils.getParamValue('hostel', 'MAX_MEMBERS')):
            Hostel.memberList.append(newMember)
            return 'SUCCESS'
        else:
            return 'HOUSEFUL' 

    @classmethod
    def searchMember(self, memberName):        
        for idx, member in enumerate(Hostel.memberList):
            if member.name == memberName:
                return idx
        return -1

    @classmethod        
    def getDuesOfMember(self, memberName):
        idxMember = Hostel.searchMember(memberName=memberName)
        #print(memberName, idxMember)
        if idxMember == -1:
            return 'MEMBER_NOT_FOUND'
        else:
            return Hostel.memberList[idxMember].dues
        
            
    @classmethod
    def removeMember(self, memberName):
        #print(memberName)
        idxMember = Hostel.searchMember(memberName=memberName)
        if idxMember == -1:
            return 'MEMBER_NOT_FOUND' 
        else:
            if Hostel.memberList[idxMember].totaldues != 0:
                return 'FAILURE'
            else:
                Hostel.memberList.pop(idxMember)
                #for idx, member in enumerate(Hostel.memberList):
                #    del Hostel.memberList[idx].dues[memberName]
                return 'SUCCESS'
        

    @classmethod        
    def getMembers(self):
        for member in Hostel.memberList:
            print(member.getDetails())
    
