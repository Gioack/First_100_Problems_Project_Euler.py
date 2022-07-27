from urllib.request import urlopen


class path_sum_three_ways():
    def __init__(self):
        self.matrix = self.get_matrix()

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
        dimension = 80
        paths = [self.matrix[i][-1] for i in range(dimension)]
        for i in range(dimension-2, -1, -1):
            paths[0] += self.matrix[0][i]
            for j in range(1, dimension):
                paths[j] = min(paths[j], paths[j-1]) + self.matrix[j][i]
            for j in range(dimension-2, -1, -1):
                paths[j] = min(paths[j], paths[j+1] + self.matrix[j][i])
        return min(paths)


print(path_sum_three_ways().main())
