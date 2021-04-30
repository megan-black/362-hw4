import unittest
import average

class TestCase(unittest.TestCase):
    def test_good(self):
        self.assertEqual(average.avgs([2,3,4]), 3.0)
    def test_excep(self):
        self.assertRaises(TypeError, average.avgs, 'a')
    def test_neg(self):
        self.assertRaises(ZeroDivisionError, average.avgs, [])
            
if __name__ == "__main__":
    unittest.main(verbosity=2)