def product_sum_numbers(product, Sum, number_of_factors, start):
    k = product - Sum + number_of_factors
    if k < kmax:
        if product < n[k]:
            n[k] = product
        for i in range(start, kmax//product*2 + 1):
            product_sum_numbers(product*i, Sum+i, number_of_factors+1, i)


kmax = 12000
n = [2*kmax] * kmax
product_sum_numbers(1, 1, 1, 2)
print(sum(set(n[2:])))
