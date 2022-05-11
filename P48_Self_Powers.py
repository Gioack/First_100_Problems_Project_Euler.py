def Self_Powers():
    Sum = 0
    for x in range(1,1001):
        Sum += x**x
    return str(Sum)[-10:]
print(Self_Powers())