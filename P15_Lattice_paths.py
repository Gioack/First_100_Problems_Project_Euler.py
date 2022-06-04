from math import factorial


def lattice_paths():
    # It can be solved easily with this mathematical formula
    return int(factorial(40)/(factorial(20)*factorial(20)))


print(lattice_paths())
