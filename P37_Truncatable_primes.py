class truncatable_primes():
    primes_as_bools = []

    def add_primes(self, until):
        self.primes_as_bools = [True for i in range(until + 1)]
        p = 2
        while (p * p <= until):
            if (self.primes_as_bools[p] == True):
                for i in range(p ** 2, until + 1, p):
                    self.primes_as_bools[i] = False
            p += 1
        self.primes_as_bools[0] = False
        self.primes_as_bools[1] = False

    def is_prime(self, num):
        return self.primes_as_bools[num]

    def is_truncable_from_left(self, number):
        while number != "":
            if self.is_prime(int(number)) == False:
                return False
            number = str(number)[1:]
        return True

    def is_truncable_from_right(self, number):
        while number != "":
            if self.is_prime(int(number)) == False:
                return False
            number = str(number)[:-1]
        return True

    def is_truncable(self, number):
        return (self.is_truncable_from_left(number)) and (self.is_truncable_from_right(number))

    def get_sum_of_truncable_primes(self):
        sum_truncable_primes = list()
        for prime, bool in enumerate(self.primes_as_bools):
            if bool == True:
                if prime < 10:
                    continue
                if self.is_truncable(prime):
                    sum_truncable_primes.append(prime)
        return sum(sum_truncable_primes)


s = truncatable_primes()
s.add_primes(1000000)
print(s.get_sum_of_truncable_primes())
