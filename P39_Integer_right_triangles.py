def pythagoreanTriplets():
    triplets = dict()
    for a in range(1, 500):
        for b in range(1, 500):
            c = (a**2 + b**2)**0.5
            if int(c) == c:
                sum_a_b_c = a + b + c
                triplets[int(sum_a_b_c)] = triplets.get(sum_a_b_c, 0) + 1
    most_seen_sum = max(triplets.values())
    for key, value in triplets.items():
        if value == most_seen_sum:
            return key


print(pythagoreanTriplets())
