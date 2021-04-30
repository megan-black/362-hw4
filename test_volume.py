import unittest
import volume

class TestCase(unittest.TestCase):
    def test_good(self):
        self.assertEqual(volume.vol(5), 125)
    def test_excep(self):
        self.assertRaises(TypeError, volume.vol, 'a')
    def test_neg(self):
        self.assertLessEqual(volume.vol(0), volume.vol(-5))
            
if __name__ == "__main__":
    unittest.main(verbosity=2)