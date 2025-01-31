import unittest
from main import tablice, slowniki

class TestMainFunctions(unittest.TestCase):

    def test_tablice_output(self):
        number, normal_times, comprehension_times = tablice()
        self.assertEqual(len(number), 4)  # tutaj jest aby test sie rozjebal
        self.assertEqual(len(normal_times), 5)
        self.assertEqual(len(comprehension_times), 5)

    def test_slowniki_output(self):
        number, normal_times, comprehension_times = slowniki()
        self.assertEqual(len(number), 5)
        self.assertEqual(len(normal_times), 5)
        self.assertEqual(len(comprehension_times), 5)

    def test_tablice_equality(self):
        number, normal_times, comprehension_times = tablice()
        self.assertTrue(all(isinstance(t, float) for t in normal_times))
        self.assertTrue(all(isinstance(t, float) for t in comprehension_times))

    def test_slowniki_equality(self):
        number, normal_times, comprehension_times = slowniki()
        self.assertTrue(all(isinstance(t, float) for t in normal_times))
        self.assertTrue(all(isinstance(t, float) for t in comprehension_times))

if __name__ == '__main__':
    unittest.main()