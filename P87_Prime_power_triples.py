from sympy import primerange


def prime_power_triples():
    triplets_that_respect_rule = set()
    squares = [x**2 for x in primerange(2, 100000) if x**2 < 50000000]
    cubes = [x**3 for x in primerange(2, 100000) if x**3 < 50000000]
    fourth_powers = [x**4 for x in primerange(2, 100000) if x**4 < 50000000]
    for square in squares:
        for cube in cubes:
            for fourth_power in fourth_powers:
                total = square+cube+fourth_power
                if total < 50000000:
                    triplets_that_respect_rule.add(total)
    return len(triplets_that_respect_rule)


print(prime_power_triples())
