class magic_5_gon_ring():
    def main(self):
        result = 0
        for total in range(1, 31):
            maximum_arrangement_of_total = self.get_maximum_arrangement_of_total(
                total)
            if maximum_arrangement_of_total > result:
                result = maximum_arrangement_of_total
        return result

    def get_all_arrangements_to_make(self, n):
        arrangements = list()
        for a in range(1, 11):
            for b in range(1, 11):
                for c in range(1, 11):
                    if (a+b+c == n):
                        arrangements.append([a, b, c])
        return arrangements

    def group_by_central_number(self, arrangements):
        grouped = dict()
        for way in arrangements:
            if way[1] in grouped:
                grouped[way[1]] += [way]
            else:
                grouped[way[1]] = [way]
        return grouped

    def get_maximum_arrangement_of_total(self, total):
        self.all_arrangements = self.get_all_arrangements_to_make(total)
        self.arrangements_grouped_by_central_number = self.group_by_central_number(
            self.all_arrangements)
        maximum = self.get_maximum_by_calculating_all_arrangements()
        return maximum

    def get_maximum_by_calculating_all_arrangements(self):
        maximum = 0
        for line_1 in self.all_arrangements:
            for line_2 in self.arrangements_grouped_by_central_number[line_1[2]]:
                for line_3 in self.arrangements_grouped_by_central_number[line_2[2]]:
                    for line_4 in self.arrangements_grouped_by_central_number[line_3[2]]:
                        for line_5 in self.arrangements_grouped_by_central_number[line_4[2]]:
                            if line_5[2] == line_1[1]:
                                result = self.order_starting_lowest_external_node(line_1, line_2, line_3,
                                                                                  line_4, line_5)
                                result_string = self.to_string(
                                    self.flatten(result))
                                if len(result_string) == 16 and self.contains_all_digits(result):
                                    if int(result_string) > maximum:
                                        maximum = int(result_string)
        return maximum

    def order_starting_lowest_external_node(self, *result):
        minimal_first_number = None
        for index, list in enumerate(result):
            if minimal_first_number == None or list[0] < minimal_first_number:
                minimal_first_number = list[0]
                index_of_list_with_minimal_external = index
        ordered_result = result[index_of_list_with_minimal_external:] + \
            result[:index_of_list_with_minimal_external]
        return ordered_result

    def to_string(self, list):
        return ''.join(str(v) for v in (list))

    def contains_all_digits(self, result):
        return sorted(set(self.flatten(result))) == [x for x in range(1, 11)]

    def flatten(self, xss):
        return [x for xs in xss for x in xs]


print(magic_5_gon_ring().main())
