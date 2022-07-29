def count_letter(number):
    number = str(number)
    if len(number) == 1:
        return count_letter_1_digits(number)
    elif len(number) == 2:
        return count_letter_2_digits(number)
    elif len(number) == 3:
        return count_letter_3_digits(number)


def count_letter_1_digits(number):
    unit_letter_count = {"1": 3, "2": 3, "3": 5, "4": 4,
                         "5": 4, "6": 3, "7": 5, "8": 5, "9": 4, "0": 0}
    return unit_letter_count[number]


def count_letter_2_digits(number):
    tens = number[0]
    unit = number[1]
    exceptions_count = {
        "10": 3, "11": 6, "12": 6, "13": 8,
        "14": 8, "15": 7, "16": 7, "17": 9, "18": 8, "19": 8}
    tens_letter_count = {"1": 3, "2": 6, "3": 6, "4": 5,
                         "5": 5, "6": 5, "7": 7, "8": 6, "9": 6, "0": 0}
    if 10 < int(number) < 20:
        return exceptions_count[number]
    else:
        return tens_letter_count[tens]+count_letter_1_digits(unit)


def count_letter_3_digits(number):
    hundreds = number[0]
    tens_unit = number[1:]
    count_tens_and_unit = count_letter_2_digits(tens_unit)
    count_hundreds = count_letter_1_digits(
        hundreds)+len("hundred")
    count_letters = count_hundreds+count_tens_and_unit
    if count_tens_and_unit != 0:
        count_letters += len("and")
    return count_letters


def number_letter_counts():
    counter = 11  # it's not 0 because we count manually one thousand
    for x in range(1, 1000):
        counter += count_letter(x)
    return counter


print(count_letter(21))
print(number_letter_counts())
