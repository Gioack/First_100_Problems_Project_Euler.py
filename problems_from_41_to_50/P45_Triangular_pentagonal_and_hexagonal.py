def triangular_pentagonal_and_hexagonal():
    hexagonal_numbers = {n*(2*n-1) for n in range(144, 30000)}
    pentagonal_numbers = {n*(3*n-1)/2 for n in range(166, 35000)}
    triangular_numbers = {n*(n+1)/2 for n in range(286, 60000)}
    return hexagonal_numbers.intersection(pentagonal_numbers, triangular_numbers)


print(triangular_pentagonal_and_hexagonal())
