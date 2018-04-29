import unittest
from src.RomanNumerals import RomanNumerals


class test_RomanNumerals(unittest.TestCase):
    def test_one(self):
        rm = RomanNumerals()
        self.assertEqual(rm.convert("1"), "I")

    @unittest.skip("not yet implemented")
    def test_two(self):
        rm = RomanNumerals()
        self.assertEqual(rm.convert("2"), "II")

    @unittest.skip("not yet implemented")
    def test_three(self):
        rm = RomanNumerals()
        self.assertEqual(rm.convert("3"), "III")

    @unittest.skip("not yet implemented")
    def test_four(self):
        rm = RomanNumerals()
        self.assertEqual(rm.convert("4"), "IV")

    @unittest.skip("not yet implemented")
    def test_five(self):
        rm = RomanNumerals()
        self.assertEqual(rm.convert("5"), "V")

    @unittest.skip("not yet implemented")
    def test_six(self):
        rm = RomanNumerals()
        self.assertEqual(rm.convert("6"), "VI")


if __name__ == '__main__':
    unittest.main()
