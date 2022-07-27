def prime_summations(limit):
    ways_to_make_numbers = {x: 0 for x in range(limit)}
    ways_to_make_numbers[0] = 1
    available_numbers = [x for x in range(1, limit)]
    for available_number in available_numbers:
        for number in ways_to_make_numbers:
            if number >= available_number:
                ways_to_make_numbers[number] += ways_to_make_numbers[number-available_number]
    for number, ways in ways_to_make_numbers.items():
        if ways % 1000000 == 0:
            return number


print(prime_summations(80000))
