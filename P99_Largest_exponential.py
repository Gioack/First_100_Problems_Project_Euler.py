from math import log
from urllib.request import urlopen


class largest_exponential:
    def __init__(self):
        self.numbers = self.read_online_file(
            "https://projecteuler.net/project/resources/p099_base_exp.txt")

    def read_online_file(self, url):
        text = urlopen(url)
        text = str(text.read(), 'utf-8').rstrip()
        text = text.split()
        return text

    def main(self):
        biggest_number_of_digits = 0
        line_of_biggest_number = 0
        for line, number in enumerate(self.numbers):
            number_digits = self.get_number_of_digits(number)
            if number_digits > biggest_number_of_digits:
                biggest_number_of_digits = number_digits
                line_of_biggest_number = line+1
        return line_of_biggest_number

    def get_number_of_digits(self, exponential):
        base, exponent = map(int, exponential.split(","))
        number_digits = 1+exponent*log(base, 10)
        return number_digits


print(largest_exponential().main())
