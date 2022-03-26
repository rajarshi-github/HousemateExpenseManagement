import os

from operation import *
from getdues import *
from cleardues import *
from moveinout import *
from spend import *
from readInputs import readInputs
from hostel import Hostel
from constants import sep

class expenses():

    def __init__(self, listOfTests):
        self.testcases = listOfTests

    def do(self):
        for filename in self.testcases:

            lstOfCommands = readInputs( filename)

            for command in lstOfCommands():
                try:
                    clsName = globals()[ operationToClassMapping(command[0]) ]

                    if clsName(command).isValid() and \
                        clsName(command).hasValidArguments():

                        status = clsName(command).do()
                        if status is not None:
                            print(status)
                except NotEnoughHouseMates as e:
                    print('MEMBER_NOT_FOUND')

if __name__ == '__main__':
    #listOfTests = ['test1.txt']
    #listOfTests = ['test4.txt']
    listOfTests = ['test5.txt']

    expenses(listOfTests=listOfTests).do()
