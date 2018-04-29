import pytest
from src.RomanNumerals import RomanNumerals


class TestRomanNumerals:
    def test_one(self):
        rm = RomanNumerals()
        assert rm.convert(1) == "I"

    def test_two(self):
        rm = RomanNumerals()
        assert rm.convert(2) == "II"

    def test_three(self):
        rm = RomanNumerals()
        assert rm.convert(3) == "III"

    def test_four(self):
        rm = RomanNumerals()
        assert rm.convert(4) == "IV"

    def test_five(self):
        rm = RomanNumerals()
        assert rm.convert(5) == "V"

    @pytest.mark.skip()
    def test_six(self):
        rm = RomanNumerals()
        assert rm.convert(6) == "VI"
