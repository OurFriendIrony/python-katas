class RomanNumerals:
    def convert(self, input):
        roman_string = ""
        if input == 4:
            roman_string = "IV"
        elif input == 5:
            roman_string = "V"
        else:
            for x in range(0, input):
                roman_string += "I"

        return roman_string
