class square_digit_chains():
    does_number_arrive_at_89 = dict()

    def main(self):
        number_chains_arrive_at_89 = 0
        for i in range(2, 10**7):
            if self.does_chain_arrive_at_89(i):
                number_chains_arrive_at_89 += 1
        return number_chains_arrive_at_89

    def does_chain_arrive_at_89(self, number):
        original_number = number
        while True:
            number = self.get_sum_squares_its_digits(number)
            if number in self.does_number_arrive_at_89:
                self.does_number_arrive_at_89[original_number] = self.does_number_arrive_at_89[number]
                return self.does_number_arrive_at_89[number]
            if number == 1:
                self.does_number_arrive_at_89[original_number] = False
                return False
            if number == 89:
                self.does_number_arrive_at_89[original_number] = True
                return True

    def get_sum_squares_its_digits(self, number):
        sum_squares_its_digits = 0
        for digit in str(number):
            sum_squares_its_digits += int(digit)**2
        return sum_squares_its_digits


print(square_digit_chains().main())
