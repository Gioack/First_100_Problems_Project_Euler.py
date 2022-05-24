def isprime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def _10001st_prime():
    counter_of_primes = 0
    x = 2
    while True:
        if isprime(x):
            counter_of_primes += 1
        if counter_of_primes == 10001:
            return x
        x += 1


print(_10001st_prime())
