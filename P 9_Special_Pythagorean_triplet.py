def special_pythagorean_triplet():
    m = 2
    while True:
        for n in range(1, m):
            a = (m ** 2) - (n ** 2)
            b = 2 * m * n
            c = (m ** 2) + (n ** 2)
            sum_triplet = a + b + c
            if sum_triplet == 1000:
                return a*b*c
        m += 1


print(special_pythagorean_triplet())
