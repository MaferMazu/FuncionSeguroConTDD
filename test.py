import unittest
import datetime
from Person import Person

class TestPension(unittest.TestCase):
    def TestPensionMale60And750Quot(self):
        date = datetime.datetime(1996, 2, 13)
        p=Person("Pedro","M",date,750)
        p.AbleIVSSPension()

if __name__ == '__main__':
    unittest.main()
