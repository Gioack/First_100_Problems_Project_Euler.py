from sympy import divisors


def highly_divisible_triangular_number():
    triangle_number = 28
    number_of_triangle_number = 7
    while True:
        if len(divisors(triangle_number)) > 500:
            return triangle_number
        number_of_triangle_number += 1
        triangle_number += number_of_triangle_number


print(highly_divisible_triangular_number())
