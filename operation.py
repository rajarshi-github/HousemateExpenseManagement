from genericUtils import Utils
from hostel import Hostel
from exceptions import NotEnoughHouseMates

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
    