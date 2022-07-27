def almost_equilateral_triangles():
    previous_side = 1
    following_side = 1
    perimeter = 0
    m = 1
    sum_perimeters = 0
    while perimeter <= 10**9:
        previous_side, following_side = following_side, \
            4 * following_side - previous_side + 2*m
        m = -m
        sum_perimeters += perimeter
        perimeter = 3*following_side - m
    return sum_perimeters


print(almost_equilateral_triangles())
