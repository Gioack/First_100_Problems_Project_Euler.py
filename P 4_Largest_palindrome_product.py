def Is_Palindrom(x):
    return str(x)[::-1] == str(x)
def Largest_palindrome_product():
    Largest = 0
    for x in range(100,1000):
        for y in range(100,1000):
            if (Is_Palindrom(x*y)) and (x*y>Largest):
                Largest = x*y
    return Largest 
print(Largest_palindrome_product()) 
    