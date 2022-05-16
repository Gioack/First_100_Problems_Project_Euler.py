def self_powers():
    sum_numbers = 0
    for x in range(1,1001):
        sum_numbers += x**x
    return str(sum_numbers)[-10:]


print(self_powers())