import unittest
import name

class TestCase(unittest.TestCase):
    def test_good(self):
        self.assertEqual(name.fullname('Megan', 'Black'), 'Megan Black')
    def test_excep(self):
        self.assertRaises(TypeError, name.fullname, (3, 4))
    def test_neg(self):
        self.assertRaises(TypeError, name.fullname, 'm')
            
if __name__ == "__main__":
    unittest.main(verbosity=2)