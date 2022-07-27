class number_spiral_diagonals():
    sum_of_diagonals = 1
    last_corner_number = 1
    numbers_that_need_to_be_added = 1000*2
    counter_corner = 0
    number_to_add_to_switch_corner = 2

    def sum_diagonals(self):
        while self.numbers_that_need_to_be_added > 0:
            if self.is_last_number_right_up_corner():
                self.increase_number_to_add()
            self.switch_corner()
            self.add_to_sum()
            self.numbers_that_need_to_be_added -= 1
        return self.sum_of_diagonals

    def is_last_number_right_up_corner(self):
        return self.counter_corner == 4

    def increase_number_to_add(self):
        self.counter_corner = 0
        self.number_to_add_to_switch_corner += 2

    def switch_corner(self):
        self.last_corner_number += self.number_to_add_to_switch_corner
        self.counter_corner += 1

    def add_to_sum(self):
        self.sum_of_diagonals += self.last_corner_number


print(number_spiral_diagonals().sum_diagonals())
