from itertools import combinations, permutations
import operator


class arithmetic_expressions():
    operations = [operator.add, operator.sub, operator.mul, operator.truediv]
    sets = list()

    def __init__(self):
        self.sets = combinations(range(1, 10), 4)

    def main(self):
        longest_consecutive = 0
        for set in self.sets:
            obtainable_numbers = self.get_all_obtainable_numbers(set)
            consecutive_of_set = self.calculate_consecutive_numbers(
                obtainable_numbers)
            if consecutive_of_set > longest_consecutive:
                longest_consecutive = consecutive_of_set
                best_set = set
        return "".join(map(str, best_set))

    def get_all_obtainable_numbers(self, numbers):
        results = set()
        for numbers in permutations(numbers):
            for index_operation in combinations(list(range(4))*3, 3):
                for permutation_index in permutations(index_operation):
                    item_0 = numbers[0]
                    item_1 = numbers[1]
                    item_2 = numbers[2]
                    item_3 = numbers[3]
                    result_route_1 = self.get_result_route_1(
                        permutation_index, item_0, item_1, item_2, item_3)
                    result_route_2 = self.get_result_route_2(
                        permutation_index, item_0, item_1, item_2, item_3)
                    if float(result_route_1).is_integer() and result_route_1 >= 1:
                        results.add(int(result_route_1))
                    if float(result_route_2).is_integer() and result_route_2 >= 1:
                        results.add(
                            int(result_route_2))
        return sorted(results)

    def get_result_route_1(self, permutation_index, item_0, item_1, item_2, item_3):
        first_operation_result = self.operations[permutation_index[0]](
            item_0, item_1)
        second_operation_result = self.operations[permutation_index[1]](
            item_2, item_3)
        result_route_1 = abs(self.operations[permutation_index[2]](
            first_operation_result, second_operation_result))
        return result_route_1

    def get_result_route_2(self, permutation_index, item_0, item_1, item_2, item_3):
        try:
            first_operation_result = self.operations[permutation_index[0]](
                item_0, item_1)
            second_operation_result_2 = self.operations[permutation_index[1]](
                item_2, first_operation_result)
            result_route_2 = abs(self.operations[permutation_index[2]](
                item_3, second_operation_result_2))
        except ZeroDivisionError:
            return 0
        return result_route_2

    def calculate_consecutive_numbers(self, obtainable_numbers):
        number_of_consecutive_numbers = 0
        for integer_that_should_be, integer_that_there_is in zip(range(1, len(obtainable_numbers)), obtainable_numbers):
            if integer_that_should_be == integer_that_there_is:
                number_of_consecutive_numbers += 1
            else:
                return number_of_consecutive_numbers


print(arithmetic_expressions().main())
