def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True


def get_smallest_prime_divisor(number):
    divisor_prime = 2   
    while number % divisor_prime != 0:
        divisor_prime += 1
        while not is_prime(divisor_prime):
            divisor_prime += 1
    return divisor_prime


def largest_prime_factor(number):
    largest_divisor = 1
    while number != 1:
        smallest_prime_divisor = get_smallest_prime_divisor(number)
        number /= smallest_prime_divisor
        if smallest_prime_divisor > largest_divisor:
            largest_divisor = smallest_prime_divisor
    return largest_divisor


print(largest_prime_factor(600851475143))
        
    


