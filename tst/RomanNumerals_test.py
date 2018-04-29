import pytest
from src.RomanNumerals import RomanNumerals


class TestRomanNumerals:
    @pytest.mark.skip()
    def test_one(self):
        rm = RomanNumerals()
        assert rm.convert("1") == "I"

    @pytest.mark.skip()
    def test_two(self):
        rm = RomanNumerals()
        assert rm.convert("2") == "II"

    @pytest.mark.skip()
    def test_three(self):
        rm = RomanNumerals()
        assert rm.convert("3") == "III"

    @pytest.mark.skip()
    def test_four(self):
        rm = RomanNumerals()
        assert rm.convert("4") == "IV"

    @pytest.mark.skip()
    def test_five(self):
        rm = RomanNumerals()
        assert rm.convert("5") == "V"

    @pytest.mark.skip()
    def test_six(self):
        rm = RomanNumerals()
        assert rm.convert("6") == "VI"
