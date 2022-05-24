def get_input():
    triangle = ["75", "95 64", "17 47 82", "18 35 87 10", "20 04 82 47 65", "19 01 23 75 03 34", "88 02 77 73 07 63 67", "99 65 04 28 06 16 70 92", "41 41 26 56 83 40 80 70 33", "41 48 72 33 47 32 37 16 94 29",
                "53 71 44 65 25 43 91 52 97 51 14", "70 11 33 28 77 73 17 78 39 68 17 57", "91 71 52 38 17 14 91 43 58 50 27 29 48", "63 66 04 68 89 53 67 30 73 16 69 87 40 31", "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]
    return triangle


def reverse_input_and_make_input_lists(triangle):
    triangle = [list(map(int, i.split())) for i in reversed(triangle)]
    return triangle


def make_each_item_its_best_route(triangle_list):
    # That's what it does:
    #     3     ->       23
    #    7 4    ->     20  19
    #   2 4 6   ->   10  13  15
    #  8 5 9 3  ->  8   5   9   3
    for index_line, line in enumerate(triangle_list):
        if index_line == 0:
            continue
        for index_number, number in enumerate(line):

            route_1 = triangle_list[index_line-1][index_number]
            route_2 = triangle_list[index_line-1][index_number+1]

            triangle_list[index_line][index_number] += max(route_1, route_2)
    return triangle_list


def maximum_path_sum_I():
    triangle = get_input()
    triangle_list = reverse_input_and_make_input_lists(triangle)
    triangle_list = make_each_item_its_best_route(triangle_list)
    return triangle_list[-1][0]


print(maximum_path_sum_I())
