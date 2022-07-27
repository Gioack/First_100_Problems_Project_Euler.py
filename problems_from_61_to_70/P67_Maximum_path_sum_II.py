import urllib.request


def open_file(url):
    return urllib.request.urlopen(url)


def make_file_reversed_list(triangle):
    triangle_list = list()
    for line in triangle:
        line = line.strip()
        line = line.decode('utf-8')
        triangle_list.append(line)
    return ([list(map(int, i.split())) for i in reversed(triangle_list)])


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


def maximum_path_sum_II():
    triangle = open_file(
        "https://projecteuler.net/project/resources/p067_triangle.txt")
    triangle_list = make_file_reversed_list(triangle)
    triangle_list = make_each_item_its_best_route(triangle_list)
    return triangle_list[-1][0]


print(maximum_path_sum_II())
