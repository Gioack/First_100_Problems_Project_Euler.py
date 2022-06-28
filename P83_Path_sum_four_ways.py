from urllib.request import urlopen


class path_sum_four_ways():
    def __init__(self):
        self.matrix = self.get_matrix()
        self.shortest_paths = {
            f"{x:02d}{y:02d}": float("inf") for x in range(len(self.matrix)) for y in range(len(self.matrix))}
        self.shortest_paths[f"{len(self.matrix)-1}{len(self.matrix)-1}"] = self.matrix[-1][-1]

    def get_matrix(self):
        matrix = self.read_online_file(
            "https://projecteuler.net/project/resources/p081_matrix.txt")
        matrix = self.parse_matrix(matrix)
        return matrix

    def read_online_file(self, url):
        text = urlopen(url)
        text = str(text.read(), 'utf-8').rstrip()
        return text

    def parse_matrix(self, matrix):
        matrix = matrix.split("\n")
        matrix = [x.split(",") for x in matrix]
        for row in matrix:
            for index, element in enumerate(row):
                row[index] = int(row[index])
        return matrix

    def main(self):
        visited = {
            f"{x:02d}{y:02d}": False for x in range(len(self.matrix)) for y in range(len(self.matrix))}
        while True:
            self.sort_paths()
            try:
                coordinates = list(filter(lambda x: x != float(
                    "inf") and visited[x] == False, self.shortest_paths.keys()))[0]
            except IndexError:
                break
            neighbors = self.get_neighbors(coordinates)
            for neighbor_coordinates in neighbors:
                neighbor_number = self.get_number_from_coordinates(
                    neighbor_coordinates)
                if self.shortest_paths[neighbor_coordinates] > neighbor_number+self.shortest_paths[coordinates]:
                    self.shortest_paths[neighbor_coordinates] = neighbor_number + \
                        self.shortest_paths[coordinates]
            visited[coordinates] = True
        return self.shortest_paths["0000"]

    def sort_paths(self):
        self.shortest_paths = {k: v for k, v in sorted(
            self.shortest_paths.items(), key=lambda item: item[1])}

    def get_number_from_coordinates(self, coordinates):
        y = int(coordinates[:2])
        x = int(coordinates[2:])
        number = self.matrix[y][x]
        return number

    def get_neighbors(self, coordinates):
        y = int(coordinates[:2])
        x = int(coordinates[2:])
        coordinates_left = self.get_number_left(y, x)
        coordinates_right = self.get_number_right(y, x)
        coordinates_up = self.get_number_up(y, x)
        coordinates_down = self.get_number_down(y, x)
        return list(filter(lambda x: x != None, [coordinates_left, coordinates_right, coordinates_up, coordinates_down]))

    def get_number_up(self, row, column):
        if row == 0:
            return None
        return f"{row-1:02d}{column:02d}"

    def get_number_down(self, row, column):
        if row == len(self.matrix)-1:
            return None
        return f"{row+1:02d}{column:02d}"

    def get_number_right(self, row, column):
        if column == len(self.matrix)-1:
            return None
        return f"{row:02d}{column+1:02d}"

    def get_number_left(self, row, column):
        if column == 0:
            return None
        return f"{row:02d}{column-1:02d}"


print(path_sum_four_ways().main())
