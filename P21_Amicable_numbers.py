def sum_of_divisors_of_each_number_to(end):
    sum_of_divisors_list = list()
    for number in range(end+1):
        sum_divisors_number = 0
        for i in range(1,round(number/2)+1):
            if number % i == 0:
                sum_divisors_number += i
        sum_of_divisors_list.append(sum_divisors_number)
    return sum_of_divisors_list


def are_amicable(number_1,sum_of_divisors_1,number_2,sum_of_divisors_2):
    return (number_1 == sum_of_divisors_2) and (sum_of_divisors_1 == number_2)


def are_different_numbers(number_1,number_2):
    return (number_1 != number_2)


def sum_all_amicable_numbers(sum_of_divisors_list):
    sum_amicable = 0
    for number_1,sum_of_divisors_1 in enumerate(sum_of_divisors_list):    
        for number_2,sum_of_divisors_2 in enumerate(sum_of_divisors_list):
            if are_amicable(number_1, sum_of_divisors_1, number_2, sum_of_divisors_2) and are_different_numbers(number_1,number_2):
                sum_amicable += (number_1+number_2)
    sum_amicable_counting_once_each_pair = sum_amicable /  2
    return int(sum_amicable_counting_once_each_pair)


def amicable_numbers():
    sum_of_divisors_list = sum_of_divisors_of_each_number_to(9999)
    sum_amicable = sum_all_amicable_numbers(sum_of_divisors_list)
    return sum_amicable


print(amicable_numbers())