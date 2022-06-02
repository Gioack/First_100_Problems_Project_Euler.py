from math import sqrt


class pentagon_numbers():
    pentagon_numbers = [1]

    def get_solution(self):
        self.create_pentagon_numbers(10000)
        for num1 in self.pentagon_numbers:
            for num2 in self.pentagon_numbers:
                if self.is_pentagonal_number(num1+num2) and self.is_pentagonal_number(abs(num1-num2)):
                    return int(abs(num1-num2))

    def is_pentagonal_number(self, n):
        k = (sqrt(24*n+1)+1)/6
        return k.is_integer()

    def create_pentagon_numbers(self, how_many_numbers):
        self.pentagon_numbers = [
            n*(3*n-1)/2 for n in range(1, how_many_numbers+1)]


s = pentagon_numbers()
print(s.get_solution())
