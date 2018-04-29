class RomanNumerals:
    ALL_ROMAN = ["IV", "V", "VI"]
    ALL_ARABIC = [4, 5, 6]

    def convert(self, input):
        roman_string = ""
        if self.ALL_ARABIC.count(input):
            roman_string = self.ALL_ROMAN[self.ALL_ARABIC.index(input)]
        else:
            for x in range(0, input):
                roman_string += "I"

        return roman_string
