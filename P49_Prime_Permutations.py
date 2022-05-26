def isprime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def prime_permutations():
    result = list()
    for x in filter(isprime, range(1000, 9999)):

        for y in range(1, 4500):

            if ((isprime(x+y)) and (isprime(x+2*y))):

                bool1 = all(((z in str(x+y)) and (z in str(x+2*y)))
                            for z in str(x))
                bool2 = all(((z in str(x)) and (z in str(x+2*y)))
                            for z in str(x+y))
                bool3 = all(((z in str(x+y)) and (z in str(x)))
                            for z in str(x+2*y))

                if bool1 and bool2 and bool3 and (x+y*2 < 10000):
                    result.append([x, x+y, x+y*2])
    return result


print(prime_permutations())
