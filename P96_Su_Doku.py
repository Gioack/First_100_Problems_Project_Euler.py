from urllib.request import urlopen


class su_doku_grid():
    def __init__(self, grid_row) -> None:
        self.rows = grid_row
        self.cols = self.get_columns()
        self.boxes = self.get_boxes()
        self.empty_spaces_coordinates = self.get_empty_spaces_coordinates()

    def get_columns(self):
        grid_cols = list()
        for column_index in range(9):
            column = list()
            for row in self.rows:
                column.append(row[column_index])
            grid_cols.append(column)
        return grid_cols

    def get_boxes(self):
        grid_boxes = list()
        for indexes_rows in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            for start, end in [[0, 3], [3, 6], [6, 9]]:
                row_1 = self.rows[indexes_rows[0]][start:end]
                row_2 = self.rows[indexes_rows[1]][start:end]
                row_3 = self.rows[indexes_rows[2]][start:end]
                box = row_1+row_2 + row_3
                grid_boxes.append(box)
        return grid_boxes

    def get_empty_spaces_coordinates(self):
        empty_spaces_coordinates = list()
        for index_row, row in enumerate(self.rows):
            for index_col, item in enumerate(row):
                if item == "0":
                    empty_spaces_coordinates.append(f"{index_row}{index_col}")
        return empty_spaces_coordinates


class su_doku():
    def __init__(self):
        self.grids = self.read_online_file(
            "https://projecteuler.net/project/resources/p096_sudoku.txt")

    def read_online_file(self, url):
        text = urlopen(url)
        text = str(text.read(), 'utf-8').rstrip()
        text = text.split("Grid")
        self.parse(text)
        return text

    def parse(self, text):
        for index, value in enumerate(text):
            text[index] = text[index].strip()
            text[index] = text[index].split("\n")
            text[index].pop(0)
        text.pop(0)
        for index, grid in enumerate(text):
            for index, row in enumerate(grid):
                grid[index] = list(grid[index])

    def main(self):
        sum_left_corner = 0
        for grid in self.grids:
            self.grid = su_doku_grid(grid)
            index = 0
            banned_numbers = {coords: list()
                              for coords in self.grid.empty_spaces_coordinates}
            while True:
                empty_space_coordinates = self.grid.empty_spaces_coordinates[index]
                self.change_cell(empty_space_coordinates, "0")
                solutions = self.get_all_numbers_that_work(
                    empty_space_coordinates)
                solutions = list(filter(
                    lambda x: x not in banned_numbers[empty_space_coordinates], solutions))
                if len(solutions) == 0:
                    index -= 1
                    banned_numbers[self.grid.empty_spaces_coordinates[index]].append(
                        self.grid.rows[int(self.grid.empty_spaces_coordinates[index][0])][int(self.grid.empty_spaces_coordinates[index][1])])
                    banned_numbers[empty_space_coordinates] = [
                    ]
                    self.change_cell(empty_space_coordinates, "0")
                else:
                    self.change_cell(empty_space_coordinates, solutions[0])
                    index += 1
                if index == len(self.grid.empty_spaces_coordinates):
                    sum_left_corner += int(
                        f"{self.grid.rows[0][0]}{self.grid.rows[0][1]}{self.grid.rows[0][2]}")
                    break
        return sum_left_corner

    def change_cell(self, empty_space_coordinates, number_to_place_there):
        coor_0 = int(empty_space_coordinates[0])
        coor_1 = int(empty_space_coordinates[1])
        self.grid.rows[coor_0][coor_1] = str(number_to_place_there)
        self.grid.cols[coor_1][coor_0] = str(number_to_place_there)
        self.grid.boxes[self.get_coor_box_from(empty_space_coordinates)][self.get_coor_in_the_box_from(
            empty_space_coordinates)] = str(number_to_place_there)

    def get_coor_in_the_box_from(self, empty_space_coordinates):
        coor_0 = int(empty_space_coordinates[0])
        coor_1 = int(empty_space_coordinates[1])
        while coor_0 > 2:
            coor_0 -= 3
        while coor_1 > 2:
            coor_1 -= 3
        translation_dictionary = {"00": 0, "01": 1, "02": 2,
                                  "10": 3, "11": 4, "12": 5,
                                  "20": 6, "21": 7, "22": 8}
        return translation_dictionary[f"{coor_0}{coor_1}"]

    def get_all_numbers_that_work(self, coordinates):
        numbers = list()
        for number in range(1, 10):
            number = str(number)
            if self.is_unique_in_row_column_box(number, coordinates):
                numbers.append(number)
        return numbers

    def is_unique_in_row_column_box(self, number, coordinates):
        row = self.grid.rows[int(coordinates[0])]
        column = self.grid.cols[int(coordinates[1])]
        box = self.grid.boxes[self.get_coor_box_from(coordinates)]
        return (number not in row) and (number not in column) and (number not in box)

    def get_coor_box_from(self, coordinates):
        range_row = self.get_box_range(int(coordinates[0]))
        range_col = self.get_box_range(int(coordinates[1]))
        dict_box = {"11": 0, "12": 1, "13": 2, "21": 3,
                    "22": 4, "23": 5, "31": 6, "32": 7, "33": 8}
        return dict_box[f"{range_row}{range_col}"]

    def get_box_range(self, number):
        if number <= 2:
            return 1
        if 3 <= number <= 5:
            return 2
        if 6 <= number <= 8:
            return 3


print(su_doku().main())
