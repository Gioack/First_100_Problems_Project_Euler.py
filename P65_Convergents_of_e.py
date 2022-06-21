from sympy import symbols


def convergents_of_e():
    period_e = [1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 1, 1, 16, 1, 1, 18, 1, 1, 20, 1, 1, 22, 1, 1, 24, 1, 1, 26, 1, 1, 28, 1, 1, 30, 1, 1, 32, 1,
                1, 34, 1, 1, 36, 1, 1, 38, 1, 1, 40, 1, 1, 42, 1, 1, 44, 1, 1, 46, 1, 1, 48, 1, 1, 50, 1, 1, 52, 1, 1, 54, 1, 1, 56, 1, 1, 58, 1, 1, 60, 1, 1, 62, 1, 1, 64, 1, 1, 66]
    # the period can be easily found here https://oeis.org/A003417
    period_e = period_e + period_e[:100-len(period_e)]
    x = symbols('x')
    expr = 2+1/x
    for y in period_e[:-2]:
        expr = expr.subs(x, y+1/x)
    result = expr.subs(x, period_e[-2])
    return sum_digits(result.numerator)


def sum_digits(result):
    sum_digits = 0
    for digit in str(result):
        sum_digits += int(digit)
    return sum_digits


print(convergents_of_e())
