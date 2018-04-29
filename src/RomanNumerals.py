class RomanNumerals:
    def convert(self, input):
        roman_string = ""
        if input == 4:
            roman_string = "IV"
        else:
            for x in range(0, input):
                roman_string += "I"

        return roman_string
