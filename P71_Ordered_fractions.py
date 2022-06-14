def ordered_fractions():
    closer_fraction = 0
    for denominator in range(1, 1000000):
        numerator = denominator*3//7
        fraction = numerator/denominator
        if fraction > closer_fraction and fraction != 3/7:
            closer_fraction = numerator/denominator
            closer_numerator = numerator
    return closer_numerator


print(ordered_fractions())
