def main():
    cubes_grouped_by_digits_they_use = group_cubes_by_digits()
    _5_permutations_of_cube = search_digits_made_by_5_cubes(
        cubes_grouped_by_digits_they_use)
    smallest_cube = min(_5_permutations_of_cube)
    return smallest_cube


def group_cubes_by_digits():
    cubes = [x**3 for x in range(10000)]
    cubes_grouped_by_digits_they_use = dict()
    for x in cubes:
        ordered_digits_x = get_ordered_digits(x)
        if ordered_digits_x in cubes_grouped_by_digits_they_use:
            cubes_grouped_by_digits_they_use[ordered_digits_x] += [x]
        else:
            cubes_grouped_by_digits_they_use[ordered_digits_x] = [x]
    return cubes_grouped_by_digits_they_use


def get_ordered_digits(number):
    return "".join(sorted(str(number)))


def search_digits_made_by_5_cubes(cubes_with_same_digits):
    for digits, list_of_numbers_with_those_digits in cubes_with_same_digits.items():
        if len(list_of_numbers_with_those_digits) == 5:
            return list_of_numbers_with_those_digits


print(main())
