def counting_fractions_in_a_range():
    counter = set()
    for denominator in range(3, 12001):
        numerator = denominator//3
        fraction = numerator/denominator
        while fraction < 1/2:
            if fraction > 1/3 and fraction < 1/2:
                counter.add(fraction)
            numerator += 1
            fraction = numerator/denominator
    return len(counter)


print(counting_fractions_in_a_range())
