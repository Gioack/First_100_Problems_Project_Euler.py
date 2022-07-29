def solution():
    lychrel_numbers = 0
    for x in range(10000+1):
        if is_lychrel(x):
            lychrel_numbers += 1
    return lychrel_numbers


def is_lychrel(number):
    sum_numbers = number
    for _ in range(50):
        sum_numbers += get_inverse(sum_numbers)
        if is_palindromic(sum_numbers):
            return False
    return True


def is_palindromic(number):
    return get_inverse(number) == number


def get_inverse(number):
    return int(str(number)[::-1])


print(solution())
