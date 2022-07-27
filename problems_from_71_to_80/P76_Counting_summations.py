def counting_summations():
    ways_to_make_numbers = {x: 0 for x in range(101)}
    ways_to_make_numbers[0] = 1
    available_numbers = [x for x in range(1, 100)]
    for available_number in available_numbers:
        for number in ways_to_make_numbers:
            if number >= available_number:
                ways_to_make_numbers[number] += ways_to_make_numbers[number-available_number]
    return ways_to_make_numbers[100]


print(counting_summations())
