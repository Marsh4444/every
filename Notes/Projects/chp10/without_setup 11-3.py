#import unittest #imported the unittest module
#from Employe import Employee#n/b python modules uses lowwer case

#class TestEmployee(unittest.TestCase):#inheritted from unittest.Testcase, this is to allow us gain access to all test methods(like assertEqual and the the rest)
#    """Test for the class Employee"""

 #   def test_employee_default_raise(self):
  #      """Do the default raise of the employee works"""
 #       employee_1 = Employee('marsh','melo', 10000)
 #       exactly_1 = employee_1.give_raise()
 #       self.assertEqual(exactly_1, 'Marsh Melo Has A Payment Of 15000')


#if __name__ == '__main__': #means “This file is being run directly, not imported.”
#    unittest.main()

#chat version
import unittest
from Employe import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def test_employee_default_raise(self):
        """Does the default raise work correctly?"""
        employee_1 = Employee('marsh', 'melo', 10000)
        result = employee_1.give_raise()
        self.assertEqual(result, 'Marsh Melo Has A Payment Of 15000')

    def test_employee_custom_raise(self):
        """Does a custom raise work correctly?"""
        employee_2 = Employee('marsh', 'melo', 10000)
        result = employee_2.give_raise(10000)
        self.assertEqual(result, 'Marsh Melo Has A Payment Of 20000')

if __name__ == '__main__':
    unittest.main()
