import unittest
from city_functions import Country_Details

class CountryTestCase(unittest.TestCase):
    """Test for 'country_details.py' """

    def test_country_details(self):
        """COuntrys like 'London, England do dey work' """
        country_info = Country_Details('london','england')
        self.assertEqual(country_info, 'London, England')


    def  test_city_country_population(self):
        """Will be able to call functions like 'population=5000000' """
        country_info = Country_Details('london', 'england- population=5000000')
        self.assertEqual(country_info, 'London, England- Population=5000000')

if __name__ == '__main__':
    unittest.main()
