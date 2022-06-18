from urllib.request import urlopen


class roman_numerals:
    def __init__(self):
        self.roman_numbers = self.read_online_file(
            "https://projecteuler.net/project/resources/p089_roman.txt")

    def read_online_file(self, url):
        text = urlopen(url)
        text = str(text.read(), 'utf-8').rstrip()
        text = text.split()
        return text

    def main(self):
        all_characters_saved = 0
        for roman_number in self.roman_numbers:
            character_saved = self.get_saved_characters(roman_number)
            all_characters_saved += character_saved
        return all_characters_saved

    def get_saved_characters(self, roman_number):
        saved_characters = 0
        if roman_number.count("IIII") == 1:
            roman_number = roman_number.replace("IIII", "IV")
            saved_characters += 2
        if roman_number.count("V") == 2:
            saved_characters += 1
        if roman_number.count("XXXX") == 1:
            roman_number = roman_number.replace("XXXX", "XL")
            saved_characters += 2
        if roman_number.count("L") == 2:
            saved_characters += 1
        if roman_number.count("CCCC") == 1:
            roman_number = roman_number.replace("CCCC", "CD")
            saved_characters += 2
        if roman_number.count("D") == 2:
            saved_characters += 1
        return saved_characters


print(roman_numerals().main())
