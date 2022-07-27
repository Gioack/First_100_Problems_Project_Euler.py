from math import sqrt


def pythagoreanTriplets():
    triplets = dict()
    for a in range(1, 500):
        for b in range(1, 500):
            c = sqrt(a**2 + b**2)
            if c.is_integer():
                sum_a_b_c = a + b + c
                triplets[int(sum_a_b_c)] = triplets.get(sum_a_b_c, 0) + 1
    most_seen_sum = max(triplets.values())
    for key, value in triplets.items():
        if value == most_seen_sum:
            return key


print(pythagoreanTriplets())
