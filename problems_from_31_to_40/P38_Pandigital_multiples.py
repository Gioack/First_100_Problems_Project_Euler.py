def is_pandigital_1_through_9(num):
    return sorted(num) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def pandigital_multiples():
    biggest_pandigital = 0
    for x in range(100000):
        concatenated_product = ""
        multiplier = 1
        while len(concatenated_product) < 9:
            concatenated_product = f"{concatenated_product}{x*multiplier}"
            multiplier += 1
        if (is_pandigital_1_through_9(concatenated_product)) and (int(concatenated_product) > biggest_pandigital):
            biggest_pandigital = int(concatenated_product)
    return biggest_pandigital


print(pandigital_multiples())
