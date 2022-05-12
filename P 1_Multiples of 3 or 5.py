def multiples_of_3_or_5():
    sum_of_multiples = 0
    for x in range(1000):
        if (x%3 == 0) or (x%5 == 0):
            sum_of_multiples += x
    return sum_of_multiples


print(multiples_of_3_or_5())
