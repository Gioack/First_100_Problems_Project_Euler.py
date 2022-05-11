from ast import Num


Numbers = [0,1]
Sum =  0
while Numbers[-1] < 4000000:
    Numbers.append(Numbers[-2]+Numbers[-1])
for x in Numbers[:-1]:
    if x % 2 == 1:
        Sum += x
print(Sum)