def counting_rectangles():
    closest_number = None
    for shape_width in range(1, 300):
        for shape_height in range(1, 300):
            number_of_rectangles = get_number_of_rectangles(
                shape_width, shape_height)
            if is_closer_to_2000000(closest_number, number_of_rectangles):
                closest_number = number_of_rectangles
                solution = shape_width*shape_height
    return solution


def is_closer_to_2000000(closest_number, number_of_rectangles):
    if closest_number == None:
        return True
    return abs(number_of_rectangles-2000000) < abs(closest_number-2000000)


def get_number_of_rectangles(shape_width, shape_height):
    return ((shape_height+1)*shape_height/2) * \
        ((shape_width+1)*shape_width/2
         )


print(counting_rectangles())
