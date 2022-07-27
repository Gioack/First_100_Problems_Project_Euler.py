from urllib.request import urlopen
from itertools import product


class XOR_decryption():
    def __init__(self):
        self.message = self.read_online_file(
            "https://projecteuler.net/project/resources/p059_cipher.txt")

    def read_online_file(self, url):
        text = urlopen(url)
        text = str(text.read(), 'utf-8')
        text = text.split(",")
        return text

    def main(self):
        for text in self.get_all_texts_that_use_English_characters():
            print(text, "\nSum:", self.get_sum_of_text_ascii_values(text), "\n\n")
        # it's so hard to teach the PC what is an
        # English file and what it's not.
        # So doing it by hands is the best option, read the texts and pick the sum of the right one

    def get_all_texts_that_use_English_characters(self):
        all_combination_that_theoretically_work = self.get_all_combinations_of_letters_that_produce_a_text_with_english_characters()
        all_text = list()
        for private_key in all_combination_that_theoretically_work:
            encrypted_message = self.encrypt_message(private_key)
            all_text.append(
                encrypted_message)
        return all_text

    def get_all_combinations_of_letters_that_produce_a_text_with_english_characters(self):
        letters_that_produce_english_letter = self.get_letters_that_produce_only_english_letter()
        all_possible_first_letters = letters_that_produce_english_letter[0]
        all_possible_second_letters = letters_that_produce_english_letter[1]
        all_possible_third_letters = letters_that_produce_english_letter[2]
        all_possible_combinations = product(
            *[all_possible_first_letters, all_possible_second_letters, all_possible_third_letters])
        return all_possible_combinations

    def get_letters_that_produce_only_english_letter(self):
        # 0 stands for the letters that work as first ones, 1 for the letters that can be second ones...
        letters_that_produce_english_letter = {0: [], 1: [], 2: []}
        for letter_position in range(3):
            for letter in range(97, 123):
                if self.always_creates_english_words(letter_position, letter):
                    letters_that_produce_english_letter[letter_position].append(
                        letter)
        return letters_that_produce_english_letter

    def always_creates_english_words(self, letter_position, private_key):
        for encrypted_letter in self.message[letter_position::3]:
            ASIIC_xor = self.XOR(encrypted_letter, private_key)
            if self.is_common_English_letter(ASIIC_xor) == False:
                return False
        return True

    def XOR(self, encrypted_letter, private_key):
        return int(encrypted_letter) ^ int(private_key)

    def is_common_English_letter(self, ASIIC_xor):
        return ASIIC_xor >= 32 and ASIIC_xor <= 122

    def encrypt_message(self, private_key):
        message_as_string = str()
        counter = 0
        for letter in self.message:
            ascii_value_decrypted = self.XOR(
                int(letter), private_key[counter % 3])
            message_as_string += chr(ascii_value_decrypted)
            counter += 1
        return message_as_string

    def get_sum_of_text_ascii_values(self, text):
        sum_of_ascii_values = 0
        for letter in text:
            sum_of_ascii_values += ord(letter)
        return sum_of_ascii_values


print(XOR_decryption().main())
