from sympy import isprime, primerange


class consecutive_prime_sum():
    primes = list(primerange(5000))
    sum_not_considered_primes = 0

    def main(self):
        longest_series = 0
        for starting_prime_position, prime in enumerate(self.primes):
            number_produces_series, length_series = self.get_max_series_info(
                starting_prime_position)
            if (length_series > longest_series):
                longest_series = length_series
                number_produces_longest_series = number_produces_series
            self.sum_not_considered_primes += prime
        return number_produces_longest_series

    def get_max_series_info(self, starting_prime_position):
        sum_considered_primes = sum(self.primes)-self.sum_not_considered_primes
        index_last_number = -1
        while not(isprime(sum_considered_primes)) or (sum_considered_primes > 1000000):
            sum_considered_primes -= self.primes[index_last_number]
            index_last_number += -1
        length_series = len(self.primes) - \
            starting_prime_position-abs(index_last_number)
        return sum_considered_primes, length_series


print(consecutive_prime_sum().main())
