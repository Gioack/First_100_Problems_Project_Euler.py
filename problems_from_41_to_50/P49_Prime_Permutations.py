def isprime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def do_numbers_have_same_digits(numbers):
    a, b, c = numbers[0], numbers[1], numbers[2]
    for digit in str(a):
        if (str(a).count(digit) != str(b).count(digit)) or (str(a).count(digit) != str(c).count(digit)):
            return False
    return True


def prime_permutations():
    result = list()
    for a in filter(isprime, range(1000, 5000)):
        for k in range(1, 4500):
            b = a+k
            c = a+2*k
            if isprime(b) and isprime(c) and do_numbers_have_same_digits([a, b, c]):
                result.append([a, b, c])
    return result


print(prime_permutations())
