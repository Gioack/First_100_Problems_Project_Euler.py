from sympy import divisors 


def get_abudant_numbers():
    abudant_numbers = list()
    for i in range(12,20162): # we can use 20162 istead of 28123 each time because 20162 is the real limit  
        if sum(divisors(i)[:-1]) > i:
            abudant_numbers.append(i)
    return abudant_numbers
    
    
def get_all_possible_sums():
    abudant_numbers = get_abudant_numbers()
    all_sum = set()
    for i in abudant_numbers:
        for j in abudant_numbers:
            if (i+j) > 20162 :
                break
            all_sum.add(i+j)
    return all_sum
            

def check_the_numbers_that_are_not_sums_of_abundants():
    all_possible_sums = get_all_possible_sums()
    sum_of_numbers_that_are_not_a_sum_of_2_abundant_numbers = 0
    for i in range(20162):
        if i not in all_possible_sums:
            sum_of_numbers_that_are_not_a_sum_of_2_abundant_numbers += i
    return sum_of_numbers_that_are_not_a_sum_of_2_abundant_numbers


print(check_the_numbers_that_are_not_sums_of_abundants())