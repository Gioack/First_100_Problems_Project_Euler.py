def sum_square_difference():
    sum_of_the_squares = 0
    square_of_the_sum = 0
    for x in range(101):
        sum_of_the_squares += x**2
        square_of_the_sum += x
    return (square_of_the_sum**2)-(sum_of_the_squares)


print(sum_square_difference())