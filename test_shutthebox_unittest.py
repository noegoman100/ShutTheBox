import unittest
from CloseTheBoxSimulator import cover_numbers

class TestShutTheBox(unittest.TestCase):

    def setUp(self):
        pass

    def test_supersimple(self):
        thisBox = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.assertEqual(cover_numbers(6,5,thisBox), True)

if __name__ == '__main__':
    unittest.main()
