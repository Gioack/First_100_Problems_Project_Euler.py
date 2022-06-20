from sympy import divisors


class amicable_chains():
    all_sum_divisors = list()
    found_numbers = [False for x in range(10**6)]

    def __init__(self) -> None:
        self.create_all_sum_divisors()

    def create_all_sum_divisors(self):
        for x in range(10**6):
            self.all_sum_divisors.append(self.sum_of_divisors(x))

    def sum_of_divisors(self, number):
        return sum(divisors(number))-number

    def main(self):
        longest_chain = 0
        for n in range(10**6):
            if self.found_numbers[n] == False:
                chain_n = self.get_chain(n)
                if chain_n != None and len(chain_n) > longest_chain:
                    longest_chain = len(chain_n)
                    minimum_of_this_chain = min(chain_n)
        return minimum_of_this_chain

    def get_chain(self, number):
        numbers_chain = list()
        original_number = number
        number = self.all_sum_divisors[number]
        numbers_chain.append(number)
        if number == 1:
            return None
        while number != original_number:
            if number > 10**6:
                return None
            number = self.all_sum_divisors[number]
            if number in numbers_chain:
                return None
            numbers_chain.append(number)
        numbers_chain.append(original_number)
        self.mark_numbers_found_so_that_their_chain_will_not_be_computed_again(
            numbers_chain)
        return numbers_chain

    def mark_numbers_found_so_that_their_chain_will_not_be_computed_again(self, numbers_chain):
        for number in numbers_chain:
            self.found_numbers[number] = True


print(amicable_chains().main())
