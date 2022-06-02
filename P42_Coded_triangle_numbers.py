from urllib.request import urlopen


class coded_triangle_numbers():
    triangle_numbers = [1]
    last_generator_number = 1

    def get_solution(self):
        count_triangles = 0
        words = self.get_words(
            "https://projecteuler.net/project/resources/p042_words.txt")
        words = words.replace('"', "")
        words = words.split(",")
        for word in words:
            score = self.get_score(word)
            if self.is_triangle(score):
                count_triangles += 1
        return count_triangles

    def get_words(self, url):
        textpage = urlopen(url)
        text = str(textpage.read(), 'utf-8')
        return text

    def get_score(self, name):
        alphabeth_and_position = {letter: lenght for letter, lenght in zip(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27))}
        total_name = 0
        for letter in name:
            total_name += alphabeth_and_position[letter]
        return total_name

    def is_triangle(self, number):
        if number > self.triangle_numbers[-1]:
            self.add_triangle_numbers(number)
        return number in self.triangle_numbers

    def add_triangle_numbers(self, until_which_number):
        while self.triangle_numbers[-1] < until_which_number:
            self.last_generator_number += 1
            self.triangle_numbers.append(
                0.5*self.last_generator_number*(self.last_generator_number+1))


s = coded_triangle_numbers()
print(s.get_solution())
