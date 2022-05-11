def Multiples_of_3_or_5():
    Sum = 0
    for x in range(1000):
        if (x%3 == 0) or (x%5 == 0):
            Sum += x
    return Sum
print(Multiples_of_3_or_5())
