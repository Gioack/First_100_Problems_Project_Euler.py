def is_even(num):
    return num % 2 == 0


def even_fibonacci_numbers():
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < 4000000:
        fibonacci_numbers.append(
            fibonacci_numbers[-2]+fibonacci_numbers[-1])
    return sum(filter(is_even, fibonacci_numbers))


print(even_fibonacci_numbers())
