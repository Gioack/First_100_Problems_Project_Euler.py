# DO NOT EXECUTE SO HEAVY
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
# DO NOT EXECUTE SO HEAVY
def Summation_of_primes():
    Sum = 0
    for x in range(2000000):
        if isprime(x):
            Sum += x
    return Sum

# DO NOT EXECUTE SO HEAVY 
