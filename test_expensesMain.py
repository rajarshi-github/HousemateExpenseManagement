import unittest
import os
from genericUtils import Utils
from readInputs import readInputs
from constants import sep
from expensesMain import expenses

class TestTrip (unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Testing Begin ... ')
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        print('Testing Completed')
        return super().setUpClass()

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_genericUtils_1(self):
        print('Testing genericUtils ...')
        result = Utils.getInitFile()
        self.assertEqual(result, 'inmates.ini')

    def test_readInputs_1(self):
        print('Testing readInputs ...')
        trainDetails = readInputs( os.getcwd() + sep + 'test3.txt')
        self.assertEqual( trainDetails()[1][0], 'MOVE_IN')
        self.assertEqual( trainDetails()[0][0], 'MOVE_IN')
        self.assertEqual( trainDetails()[0][1], 'ANDY')
        self.assertEqual( trainDetails()[1][1], 'WOODY')

    def test_expenses_1(self):
        listOfTests = ['test3.txt']
        result = expenses(listOfTests=listOfTests).do()
        self.assertEqual( result, None)



if __name__ == '__main__':
    unittest.main()

