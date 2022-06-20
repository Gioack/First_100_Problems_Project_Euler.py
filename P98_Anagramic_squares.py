from collections import Counter
from itertools import permutations, combinations
from urllib.request import urlopen


class anagramic_squares():
    def __init__(self):
        self.words = self.read_online_file(
            "https://projecteuler.net/project/resources/p098_words.txt")

    def read_online_file(self, url):
        text = urlopen(url)
        text = str(text.read(), 'utf-8')
        text = text.replace('"', "")
        text = text.split(",")
        return text

    def main(self):
        highest_square = 0
        for word_1 in self.words:
            for word_2 in self.words:
                if word_1 != word_2 and self.are_anagram_pair(word_1, word_2):
                    if len(word_1) < len(str(highest_square)):
                        continue
                    highest_square_in_these_words = self.get_highest_square(
                        word_1, word_2)
                    if highest_square_in_these_words > highest_square:
                        highest_square = highest_square_in_these_words
        return highest_square

    def are_anagram_pair(self, a, b):
        return Counter(a) == Counter(b)

    def get_highest_square(self, word_1, word_2):
        original_word_1, original_word_2 = word_1, word_2
        highest_square = 0
        for numbers_for_replacing in combinations(list(range(10)), len(set(word_1))):
            for numbers_for_replacing_permutation in permutations(numbers_for_replacing):
                word_1, word_2 = original_word_1, original_word_2
                corresponding_numbers_of_letters = {letter: str(number) for letter, number in zip(
                    set(word_1), numbers_for_replacing_permutation)}
                word_1 = self.replace_letters_with_numbers(
                    word_1, corresponding_numbers_of_letters)
                word_2 = self.replace_letters_with_numbers(
                    word_2, corresponding_numbers_of_letters)
                if (word_1[0] == "0") or (word_2[0] == "0"):
                    continue
                if self.is_square(float(word_1)) and self.is_square(float(word_2)):
                    if max(int(word_1), int(word_2)) > highest_square:
                        highest_square = max(int(word_1), int(word_2))
        self.words.remove(original_word_1)
        return highest_square

    def replace_letters_with_numbers(self, word, way_to_replace_dict):
        for letter in set(word):
            word = word.replace(
                letter, way_to_replace_dict[letter])
        return word

    def is_square(self, number):
        return (number**0.5).is_integer()


print(anagramic_squares().main())
