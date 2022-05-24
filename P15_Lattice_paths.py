def get_factorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial


def lattice_paths():
    return get_factorial(40)/(get_factorial(20)*get_factorial(20))


print(lattice_paths())
