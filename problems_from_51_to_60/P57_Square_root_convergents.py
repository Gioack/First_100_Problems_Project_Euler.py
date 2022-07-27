from fractions import Fraction


def square_root_convergents():
    numerator = 3
    denominator = 2
    counter = 0
    for _ in range(1000):
        numerator, denominator = 2*denominator + numerator, denominator + numerator
        if _ < 10:
            print(numerator, denominator)
        if len(str(numerator)) > len(str(denominator)):
            counter += 1
    return counter


print(square_root_convergents())
