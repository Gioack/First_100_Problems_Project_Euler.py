def double_base_palindromes():
    sum_of_all_double_base_palindromes = 0
    for number in range(1000000):
        palindrom_base_10 = str(number)[::-1]
        number_base_2 = str(bin(number)[2:])
        palindrom_base_2 = number_base_2[::-1]
        if (palindrom_base_10 == str(number)) and (palindrom_base_2 == number_base_2):
            sum_of_all_double_base_palindromes += number
    return sum_of_all_double_base_palindromes


print(double_base_palindromes())
