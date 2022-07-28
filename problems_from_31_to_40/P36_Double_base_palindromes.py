def double_base_palindromes():
    sum_of_all_double_base_palindromes = 0
    for number in range(1000000):
        if is_double_base_palindrome(number):
            sum_of_all_double_base_palindromes += number
    return sum_of_all_double_base_palindromes


def is_double_base_palindrome(number):
    number_in_base_2 = to_base_2(number)
    return is_palindrome(number) and is_palindrome(number_in_base_2)


def to_base_2(number):
    return bin(number)[2:]


def is_palindrome(number):
    palindrome_base_10 = str(number)[::-1]
    return (palindrome_base_10 == number)


print(double_base_palindromes())
