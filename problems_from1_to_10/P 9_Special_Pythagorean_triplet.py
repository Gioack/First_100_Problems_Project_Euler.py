from math import sqrt


def special_pythagorean_triplet():
    for a in range(1, 500):
        for b in range(1, 500):
            c = sqrt(a**2 + b**2)
            if c.is_integer():
                sum_a_b_c = a + b + c
                if sum_a_b_c == 1000:
                    return int(a*b*c)


print(special_pythagorean_triplet())
