class number_spiral_diagonals():
    sum_of_diagonals = 101
    last_number = 25
    numbers_that_need_to_be_added = 996*2
    counter = 0
    number_to_add = 6

    def sum_diagonals(self):
        while self.numbers_that_need_to_be_added > 0:
            if self.is_last_number_right_up_corner():
                self.increase_number_to_add()
            self.switch_corner()
            self.counter += 1
            self.numbers_that_need_to_be_added -= 1
        return self.sum_of_diagonals

    def is_last_number_right_up_corner(self):
        return self.counter == 4

    def increase_number_to_add(self):
        self.counter = 0
        self.number_to_add += 2

    def switch_corner(self):
        self.last_number += self.number_to_add
        self.sum_of_diagonals += self.last_number


c = number_spiral_diagonals()
print(c.sum_diagonals())
