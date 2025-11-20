"""
the unittest automatically runs  before each test method the setup() method is called first
then one test method runs, then python clears things and repeats for the next test
"""
import unittest
from Employe import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""

    def setup(self): #special method that helps us avoid repetition.
        """
        Create name and payment set the response also
        """
        self.employee_1 = Employee('marsh','melo',10000)
        
    def  test_give_default_raise(self):
        """adds default raise"""
        result = self.employee_1.give_raise()
        self.assertEqual(result, 'Marsh Melo Has A Payment Of 15000')
        
    def test_give_custom_raise(self):
        """Adds custom raise"""
       result = self.employee_1.give_raise(10000)
       self.asserEqual(result, 'Marsh Melo Has A Payment Of 20000')

if __name__ = '__main__':
    unittest.main()
