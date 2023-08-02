import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wohuh', 'uigyg', 'guyftf')
        self.assertEqual(formatted_name, 'Wohuh Guyftf Uigyg')


if __name__ == '__main__':
    unittest.main()

# unittest.main()