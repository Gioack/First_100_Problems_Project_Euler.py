from itertools import product


def distinct_powers():
    a = [x for x in range(2,101)]
    b = [x for x in range(2,101)]
    distinct_terms = set()
    for x,y in product(a,b):
        distinct_terms.add(x**y)
    return len(distinct_terms)


print(distinct_powers())