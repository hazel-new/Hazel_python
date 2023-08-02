import unittest
from city_functions import cities


class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        city_info = cities('shanghai', 'china')
        self.assertEqual(city_info, 'Shanghai,China')

    def test_city_country_population(self):
        city_info = cities('shanghai', 'china', 10000)
        self.assertEqual(city_info, 'Shanghai,China - population 10000')


if __name__ == '__main__':
    unittest.main()