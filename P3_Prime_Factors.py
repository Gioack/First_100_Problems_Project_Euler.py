def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def Prime_Factors():
    Result = list()
    x = 600851475143
    y = 0 
    for y in range(1,100000):
        if (x % y == 0) and (isprime(y)):
            x = x/y
            Result.append(y)
    return max(Result)
print(Prime_Factors())
        
    


