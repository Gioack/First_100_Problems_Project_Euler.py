class sequence():
    def __init__(self, start, end):
        self.start = start
        self.end = end


def is_pandigital_1_through_9(num):
    return sorted(num) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def get_products(sequence1, sequence2):
    sum_of_products_whose_multiplicand_multiplier_product_are_a_1_through_9_pandigital = set()
    for x in range(sequence1.start, sequence1.end):
        for y in range(sequence2.start, sequence2.end):
            product = x*y
            if is_pandigital_1_through_9(f"{x}{y}{product}"):
                sum_of_products_whose_multiplicand_multiplier_product_are_a_1_through_9_pandigital.add(product)
    return sum_of_products_whose_multiplicand_multiplier_product_are_a_1_through_9_pandigital


def pandigital_products():
    sum_of_products_whose_multiplicand_multiplier_product_are_a_1_through_9_pandigital = get_products(sequence(1, 10000), sequence(1, 10))
    sum_of_products_whose_multiplicand_multiplier_product_are_a_1_through_9_pandigital.update(get_products(sequence(100, 1000), sequence(10, 100)))
    return sum(sum_of_products_whose_multiplicand_multiplier_product_are_a_1_through_9_pandigital)


print(pandigital_products())