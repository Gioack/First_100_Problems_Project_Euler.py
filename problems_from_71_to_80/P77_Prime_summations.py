from sympy import primerange


def prime_summations():
    ways_to_make_numbers = {x: 0 for x in range(100)}
    ways_to_make_numbers[0] = 1
    available_numbers = primerange(100)
    for available_number in available_numbers:
        for number in ways_to_make_numbers:
            if number >= available_number:
                ways_to_make_numbers[number] += ways_to_make_numbers[number-available_number]
    for number, ways in ways_to_make_numbers.items():
        if ways > 5000:
            return number


print(prime_summations())
