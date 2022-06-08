from math import factorial


def combinatoric_selections():
    counter = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            value = factorial(n)/(factorial(r)*factorial(n-r))
            if value > 1000000:
                counter += 1
    return counter


print(combinatoric_selections())
