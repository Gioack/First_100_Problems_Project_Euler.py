from itertools import permutations


def lexicographic_permutations():
    for count, permutation in enumerate(permutations("0123456789")):
        if count == 999999:
            return "".join(permutation)


print(lexicographic_permutations())
