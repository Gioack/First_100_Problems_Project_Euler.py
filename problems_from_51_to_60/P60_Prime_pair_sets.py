from sympy import isprime, primerange


class prime_pair_sets():
    primes = list(primerange(10000))
    all_primes_with_which_key_concatenate_in_prime = {
        prime: set() for prime in primes}

    def solution(self):
        self.create_all_primes_with_which_key_concatenate_in_prime()
        self.get_sums_of_all_sets()
        return min(self.sums_of_all_sets)

    def create_all_primes_with_which_key_concatenate_in_prime(self):
        for prime1 in self.primes:
            for prime2 in self.primes:
                if self.concatanate_in_a_prime_in_any_order(prime1, prime2):
                    self.all_primes_with_which_key_concatenate_in_prime[prime1].add(
                        prime2)

    def concatanate_in_a_prime_in_any_order(self, a, b):
        return self.concatenate_in_a_prime(a, b) and self.concatenate_in_a_prime(b, a)

    def concatenate_in_a_prime(self, a, b):
        return isprime(int(str(a)+str(b)))

    def get_sums_of_all_sets(self):
        self.sums_of_all_sets = set()
        for a, concatanable_primes_of_a in self.all_primes_with_which_key_concatenate_in_prime.items():
            for b in concatanable_primes_of_a:
                primes_with_which_a_b_concatenate_in_prime = concatanable_primes_of_a.intersection(
                    self.all_primes_with_which_key_concatenate_in_prime[b])
                if len(primes_with_which_a_b_concatenate_in_prime) >= 3:
                    if self.concatenate_in_a_prime_each_other(primes_with_which_a_b_concatenate_in_prime):
                        self.sums_of_all_sets.add(
                            sum([a, b, sum(primes_with_which_a_b_concatenate_in_prime)]))

    def concatenate_in_a_prime_each_other(self, list_of_primes):
        for x in list_of_primes:
            for y in list_of_primes:
                if x != y and not (self.concatanate_in_a_prime_in_any_order(x, y)):
                    return False
        return True


print(prime_pair_sets().solution())
