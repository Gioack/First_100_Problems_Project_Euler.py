def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True


def summation_of_primes():
    sum_of_primes = 0
    for x in range(2,2000000):
        if isprime(x):
            sum_of_primes += x
    return sum_of_primes


print(summation_of_primes())