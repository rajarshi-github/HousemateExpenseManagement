import os
from constants import sep

class readInputs:

    '''
    readMessages class
    '''
    def __init__(self, filename):
        '''
        Constructor for readMessages class
        2 attributes:
            1. filename - File name to read the test input data
            2. message - List (array) of lists 
        '''

        self.filename = filename

        try:
            with open(filename) as fileHandle:  
                self.message = [ line.rstrip().split()  for line in fileHandle.readlines()]
        except Exception:
            print("Test file " + filename + " not found")
            raise FileNotFoundError

    def messageRemoveEmpty(self):
        filterEmpty = lambda line: len(line) != 0
        self.message = list(filter( filterEmpty, self.message))

    def messegeTokenize(self):
        if self.message:
            for lineNum in range(len(self.message)):
                lineContent = self.message[lineNum]
                self.message[lineNum] = [lineContent[0], ' '.join(lineContent[1:])]

    def getMessage(self):
        self.messageRemoveEmpty()
        self.messegeTokenize()
        return self.message

    def __call__(self):
        return self.getMessage()
    


if __name__ == '__main__':

    #filenames = ['test1.txt']
    filenames = ['test1.txt', 'test2.txt']
    for filename in filenames:
        message = readInputs( os.getcwd() + sep + filename)
        print(message())

