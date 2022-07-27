def is_palindrom(x):
    return str(x)[::-1] == str(x)


def largest_palindrome_product():
    largest_product = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            product = x*y
            if (is_palindrom(product)) and (product > largest_product):
                largest_product = product
    return largest_product


print(largest_palindrome_product())
