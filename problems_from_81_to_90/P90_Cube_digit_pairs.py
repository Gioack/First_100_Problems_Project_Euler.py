from itertools import combinations


class cube_digit_pairs():
    dices = list()
    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
    number_correct_arrangements = 0

    def __init__(self) -> None:
        self.create_all_dices()

    def create_all_dices(self):
        for dice in combinations([x for x in range(10)], 6):
            dice = list(dice)
            if 6 in dice:
                dice.append(9)
            elif 9 in dice:
                dice.append(6)
            self.dices.append(dice)

    def main(self):
        for dice_1 in self.dices:
            for dice_2 in self.dices:
                self.dice_1 = dice_1
                self.dice_2 = dice_2
                if self.represent_all_squares():
                    self.number_correct_arrangements += 1
        # we divide by two because the loop count each pair twice
        return int(self.number_correct_arrangements/2)

    def represent_all_squares(self):
        for square in self.squares:
            if self.do_dices_make_square(square) == False:
                return False
        return True

    def do_dices_make_square(self, square):
        first_digit = int(square[0])
        second_digit = int(square[1])
        return (((first_digit in self.dice_1) and (second_digit in self.dice_2)) or
                ((first_digit in self.dice_2) and (second_digit in self.dice_1)))


print(cube_digit_pairs().main())
