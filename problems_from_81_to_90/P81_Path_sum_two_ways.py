from urllib.request import urlopen


class path_sum_two_ways():
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
        self.make_items_representing_their_minimal_sum_way_last_row()
        self.make_items_representing_their_minimal_sum_way_last_column()
        self.make_items_representing_their_minimal_sum_way_other_rows()
        return self.matrix[0][0]

    def make_items_representing_their_minimal_sum_way_last_row(self):
        for index in reversed(range(len(self.matrix[-1]))):
            if index == len(self.matrix)-1:
                continue
            self.matrix[-1][index] += self.matrix[-1][index+1]

    def make_items_representing_their_minimal_sum_way_last_column(self):
        for i in reversed(range(len(self.matrix))):
            if i == len(self.matrix)-1:
                continue
            self.matrix[i][-1] += self.matrix[i+1][-1]

    def make_items_representing_their_minimal_sum_way_other_rows(self):
        for index_row, row in reversed(list(enumerate(self.matrix[:-1]))):
            for index in reversed(range(len(row[:-1]))):
                number_down = self.matrix[index_row+1][index]
                number_right = self.matrix[index_row][index+1]
                self.matrix[index_row][index] += min(number_down, number_right)


if __name__ == "__main__":
    print(path_sum_two_ways().main())
