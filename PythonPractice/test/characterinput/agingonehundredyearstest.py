import unittest
from ..characterinput.agingonehundredyears import calc_future_year


class AgingOneHundredYearsTest(unittest.TestCase):

    def test_calc_future_year(self):
        self.assertEqual(2043, calc_future_year(2020, 73, 50))

if __name__ == '__main__':
    unittest.main()
