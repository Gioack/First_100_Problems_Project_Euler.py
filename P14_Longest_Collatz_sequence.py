import numpy as np
def Longest_Collatz_sequence():
    longest_counter = 0
    Number_that_produces_lonegest_counter = 0
    All_values = {x:0 for x in np.arange(2,1000000)}
    for x in np.arange(2,1000000):
        counter = 0
        Starting_value_x = x
        while x != 1:
            if x < Starting_value_x:
                All_values[Starting_value_x] = All_values[x] + counter
                break
            if x % 2 == 0:
                x /= 2
            else:
                x = 3*x+1
                counter += 1
            if x == 1:
               All_values[Starting_value_x] = counter      
        if All_values[Starting_value_x] > longest_counter:
            longest_counter = All_values[Starting_value_x]
            Number_that_produces_lonegest_counter = Starting_value_x
    return Number_that_produces_lonegest_counter
print(Longest_Collatz_sequence())