from sympy import isprime


class spiral_primes():
    all_corner_numbers = list()
    all_corner_prime_numbers = list()
    last_corner_number = 1
    counter_corner = 0
    side_lenght = 1

    def sum_diagonals(self):
        while True:
            if self.is_last_number_right_up_corner():
                self.wrap_new_layer()
            self.switch_corner()
            self.all_corner_numbers.append(self.last_corner_number)
            if isprime(self.last_corner_number):
                self.all_corner_prime_numbers.append(self.last_corner_number)
            if self.is_ratio_of_primes_below_10_percent():
                return self.side_lenght

    def is_last_number_right_up_corner(self):
        return self.counter_corner == 4

    def wrap_new_layer(self):
        self.counter_corner = 0
        self.side_lenght += 2

    def switch_corner(self):
        self.last_corner_number += self.side_lenght+1
        self.counter_corner += 1

    def is_ratio_of_primes_below_10_percent(self):
        return len(self.all_corner_prime_numbers)/len(self.all_corner_numbers) < 0.1


print(spiral_primes().sum_diagonals())
