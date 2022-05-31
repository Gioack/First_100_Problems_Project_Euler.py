def get_solution():
    number = 1
    while True:
        if does_it_have_property(number):
            return number
        number += 1


def does_it_have_property(number):
    for i in range(2, 7):
        if not do_numbers_contain_same_digits(number, number*i):
            return False
    return True


def do_numbers_contain_same_digits(num1, num2):
    num1, num2 = str(num1), str(num2)
    for digit in num1:
        if num1.count(digit) != num2.count(digit):
            return False
    return True


print(get_solution())
