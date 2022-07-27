from math import sqrt


def cuboid_route():
    limit = 1000000
    number_of_solutions = 0
    M = 2
    while number_of_solutions < limit:
        M += 1
        for i in range(3, 2*M):
            if (i*M) % 12 == 0:
                shortest_path = sqrt(i*i + M*M)
                if is_perfect_square(shortest_path):
                    number_of_solutions += min(i, M+1) - (i+1)//2
    return M


def is_perfect_square(s):
    return s.is_integer()


print(cuboid_route())
