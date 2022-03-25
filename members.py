
class Member():
    def __init__(self, name, spent=0, isLender=False, dues={}, totaldues=0):
        self.name = name
        self.spent = spent
        self.isLender = isLender
        self.dues = dues
        self.totaldues = totaldues
    
    def getDetails(self):
        return  'Name: ' + self.name \
            + ', Spent: ' + str(self.spent) \
            + ', Dues: {'  + ','.join([ k + ': ' + str(v) for k, v in self.dues.items()]) + '}' \
            + ', Totaldue: ' + str(self.totaldues)
        




