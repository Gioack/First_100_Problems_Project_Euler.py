from itertools import permutations


class cyclical_figurate_numbers():
    triangle_numbers = [n*(n+1)//2 for n in range(200)
                        if 1000 < n*(n+1)/2 < 10000]
    square_numbers = [n**2 for n in range(100) if 1000 < n**2 < 10000]
    pentagonal_numbers = [
        n*(3*n-1)//2 for n in range(100) if 1000 < n*(3*n-1)/2 < 10000]
    hexagonal_numbers = [n*(2*n-1)
                         for n in range(100) if 1000 < n*(2*n-1) < 10000]
    heptagonal_numbers = [
        n*(5*n-3)//2 for n in range(100) if 1000 < n*(5*n-3)/2 < 10000]
    octagonal_numbers = [n*(3*n-2)
                         for n in range(100) if 1000 < n*(3*n-2) < 10000]
    all_figurate_numbers = [triangle_numbers, square_numbers,
                            pentagonal_numbers, hexagonal_numbers, heptagonal_numbers, octagonal_numbers]

    def __init__(self):
        self.starting_digits_figurate_numbers = {
            n: dict() for n in range(0, 6)}
        for index, type_of_numbers in enumerate(self.all_figurate_numbers):
            for number in type_of_numbers:
                self.starting_digits_figurate_numbers[index][int(str(number)[
                    :2])] = number

    def solution(self):
        winning_set = self.generate_set()
        return sum(winning_set)

    def generate_set(self):
        for index_of_that_type, list_type_of_figurate_number in enumerate(self.all_figurate_numbers):
            for number in list_type_of_figurate_number:
                if self.starts_the_right_set(number, index_of_that_type):
                    return self.set

    def starts_the_right_set(self, number, index_of_the_type):
        indexes_of_other_figurative_numbers = list(range(6))
        indexes_of_other_figurative_numbers.remove(index_of_the_type)
        for order_of_figurative_numbers in permutations(indexes_of_other_figurative_numbers):
            try:
                self.create_potential_set(
                    number, order_of_figurative_numbers)
                if self.get_last_2_digits(self.set[5]) == self.get_first_2_digits(number):
                    return True
            except KeyError:
                continue

    def get_last_2_digits(self, number):
        return int(str(number)[2:])

    def get_first_2_digits(self, number):
        return int(str(number)[:2])

    def create_potential_set(self, number, order_of_figurative_numbers):
        self.set = [number]
        for type_figurative in order_of_figurative_numbers:
            dictionary_of_type_figurative = self.starting_digits_figurate_numbers[
                type_figurative]
            number_that_starts_with_the_end = dictionary_of_type_figurative[self.get_last_2_digits(
                self.set[-1])]
            self.set.append(number_that_starts_with_the_end)


print(cyclical_figurate_numbers().solution())
