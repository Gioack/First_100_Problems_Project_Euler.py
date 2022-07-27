class right_triangles_with_integer_coordinates():
    def __init__(self) -> None:
        self.combinations_of_coordinates = self.generate_combinations_of_coordinates()

    def generate_combinations_of_coordinates(self):
        combinations_of_coordinates = list()
        for x in range(51):
            for y in range(51):
                if x == 0 and y == 0:
                    continue
                combinations_of_coordinates.append([x, y])
        return combinations_of_coordinates

    def main(self):
        number_of_right_triangles = 0
        for P_coordinate in self.combinations_of_coordinates:
            for Q_coordinate in self.combinations_of_coordinates:
                if P_coordinate == Q_coordinate:
                    continue
                side_a, side_b, side_c = sorted(self.get_squares_of_sides(
                    P_coordinate, Q_coordinate))
                if self.is_a_right_triangle(side_a, side_b, side_c):
                    number_of_right_triangles += 1
        # we divide number_of_right_triangles by 2 because the previous algorithm counts each pair 2 times
        return int(number_of_right_triangles/2)

    def is_a_right_triangle(self, a_square, b_square, c_square):
        return c_square == a_square+b_square

    def get_squares_of_sides(self, coordinate_P, coordinate_Q):
        P_x = coordinate_P[0]
        P_y = coordinate_P[1]
        Q_x = coordinate_Q[0]
        Q_y = coordinate_Q[1]
        square_of_side_P_Q = (P_x-Q_x)**2+(P_y-Q_y)**2
        square_of_side_O_P = (P_x)**2+(P_y)**2
        square_of_side_O_Q = (Q_x)**2+(Q_y)**2
        squares_sides = [square_of_side_P_Q,
                         square_of_side_O_P, square_of_side_O_Q]
        return squares_sides


print(right_triangles_with_integer_coordinates().main())
