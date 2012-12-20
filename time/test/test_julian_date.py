import unittest
import sys
sys.path.append("../src")
from julian_date import julian_date
from time_exceptions import InputError


class TestJulianDate(unittest.TestCase):

    def setUp(self):
        # declare the test dates
        self.test_dates = [[2000,   1,  1.5,    2451545.0],
                           [1999,   1,  1.0,    2451179.5],
                           [1987,   1,  27.0,   2446822.5],
                           [1987,   6,  19.5,   2446966.0],
                           [1988,   1,  27.0,   2447187.5],
                           [1988,   6,  19.5,   2447332.0],
                           [1900,   1,  1.0,    2415020.5],
                           [1600,   1,  1.0,    2305447.5],
                           [1600,   12, 31.0,   2305812.5],
                           [1582,   10, 4.0,    2299159.5],
                           #[1582,  10, 5.0,    0],           # this should produce an error!
                           [1582,   10, 15.0,   2299160.5],
                           [837,    4,  10.3,   2026871.8],
                           [-123,   12, 31.0,   1676496.5],
                           [-122,   1,  1.0,    1676497.5],
                           [-1000,  7,  12.5,   1356001.0],
                           [-1000,  2,  29.0,   1355866.5],
                           [-1001,  8,  17.9,   1355671.4]]

    def test_julian_date(self):

        # call julian_date for each of the test dates
        # and make sure we get the correct result
        for test_set in self.test_dates:
            try:
                self.assertEqual(julian_date(test_set[0], test_set[1], test_set[2]),\
                             test_set[3])
            except InputError as i:
                print "Exception: " + i

        # check the edge condition
        self.assertRaises(InputError, julian_date, 1582, 10, 5.0)

# run the test case
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJulianDate)
    unittest.TextTestRunner(verbosity=2).run(suite)
