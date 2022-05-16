class collatz_sequence():
    collatz_of_each_number = {x:0 for x in range(2,1000000)}
    longest_lenght_of_chain = 0
    number_that_produces_longest_lenght_of_chain = 0

    def longest_collatz_sequence(self):
        for number in range(2,1000000):
            lenght_of_chain, number = self.get_lenght_chain(number)
            if self.is_the_longest(lenght_of_chain):
                self.set_longest_lenght_of_chain(lenght_of_chain)
                self.set_number_that_produces_longest_lenght_of_chain(number)

        return self.number_that_produces_longest_lenght_of_chain

    def get_lenght_chain(self, number):
        lenght_of_chain = 0
        starting_value_number = number
        while number != 1:   
            if number < starting_value_number:
                self.collatz_of_each_number[starting_value_number] = self.collatz_of_each_number[number] + lenght_of_chain
                break
            if number % 2 == 0:
                number /= 2
            else:
                number = 3*number+1
                lenght_of_chain += 1
            if number == 1:
                self.collatz_of_each_number[starting_value_number] = lenght_of_chain      
        return self.collatz_of_each_number[starting_value_number], starting_value_number

    def is_the_longest(self,lenght_of_chain):
        return lenght_of_chain > self.longest_lenght_of_chain
    
    def set_longest_lenght_of_chain(self,lenght_of_chain):
        self.longest_lenght_of_chain = lenght_of_chain

    def set_number_that_produces_longest_lenght_of_chain(self,number):
        self.number_that_produces_longest_lenght_of_chain = number


s = collatz_sequence()
print(s.longest_collatz_sequence())