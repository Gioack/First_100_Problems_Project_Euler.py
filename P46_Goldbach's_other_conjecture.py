from sympy import isprime


class goldbach_other_conjecture():
    limit = 100000
    twice_squares = [2*x**2 for x in range(limit)]

    def get_solution(self):
        for number in range(3, self.limit, 2):
            if isprime(number):
                continue
            if self.respects_goldbach_law(number) == False:
                return number

    def respects_goldbach_law(self, number):
        for i in self.twice_squares:
            if i > number:
                break
            if isprime(number-i):
                return True
        return False


print(goldbach_other_conjecture().get_solution())
