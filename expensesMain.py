import os

from operation import *
from readInputs import readInputs
from hostel import Hostel
from constants import sep

class expenses():

    def __init__(self, listOfTests):
        self.testcases = listOfTests

    def do(self):
        for filename in self.testcases:

            lstOfCommands = readInputs( os.getcwd() + sep + filename)

            for command in lstOfCommands():
                #print( f"{command=}")
                clsName = globals()[ operationToClassMapping(command[0]) ]

                #print('\n\nExecuting command : ' + clsName(command)() ) 
                if clsName(command).isValid() and \
                    clsName(command).hasValidArguments():

                    status = clsName(command).do()
                    if status is not None:
                        print(status)
                    #Hostel.getMembers()            

if __name__ == '__main__':
    #listOfTests = ['test1.txt', 'test2.txt']
    listOfTests = ['test1.txt']

    #listOfTests = ['test4.txt']
    #listOfTests = ['test5.txt']

    expenses(listOfTests=listOfTests).do()

