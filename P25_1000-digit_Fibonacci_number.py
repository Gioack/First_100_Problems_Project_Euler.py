def _1000_Digit_Fibonacci_number():
    fibonacci_numbers = [0,1]
    while len(str(fibonacci_numbers[-1])) < 1000:
        fibonacci_numbers.append(fibonacci_numbers[-2]+fibonacci_numbers[-1])
    index_of_the_first_1000_digits_number = len(fibonacci_numbers)-1
    return index_of_the_first_1000_digits_number
    
    
print(_1000_Digit_Fibonacci_number())