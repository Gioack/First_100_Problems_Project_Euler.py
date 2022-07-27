from itertools import product
from random import choice


class monopoly_odds():
    def __init__(self):
        self.dice_possibilities = list(map(
            sum, list(product(list(range(1, 5)), list(range(1, 5))))))
        self.probabilities = {key: 0 for key in range(40)}

    def main(self):
        self.run_simulation()
        _3_most_frequent_lands = self.get_3_most_frequent_lands(
            self.probabilities)
        _3_most_frequent_lands = self.to_string(_3_most_frequent_lands)
        return _3_most_frequent_lands

    def run_simulation(self):
        land = 0
        for _ in range(10**6):
            roll = choice(self.dice_possibilities)
            land = (land+roll) % 40
            land = self.get_land_considering_variables(land)
            self.probabilities[land] += 1

    def get_land_considering_variables(self, land):
        if land == 30:
            return 10
        if land == 2:
            return choice([0, 10]+[2 for _ in range(14)])
        if land == 17:
            return choice([0, 10]+[17 for _ in range(14)])
        if land == 23:
            return choice([0, 10]+[23 for _ in range(14)])
        if land == 7:
            return choice([0, 10, 11, 24, 39, 5, 15, 15, 12, 4]+[7 for _ in range(6)])
        if land == 22:
            return choice([0, 10, 11, 24, 39, 5, 25, 25, 28, 19]+[22 for _ in range(6)])
        if land == 33:
            return choice([0, 10, 11, 24, 39, 5, 35, 35, 12, 29]+[33 for _ in range(6)])
        return land

    def get_3_most_frequent_lands(self, dictionary):
        return sorted(dictionary, key=dictionary.get, reverse=True)[:3]

    def to_string(self, list):
        return "".join(map(str, list))


print(monopoly_odds().main())
