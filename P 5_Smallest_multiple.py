def smallest_multiple():
    x = 2520
    while True:
        x += 1
        for y in range(1, 21):
            if x % y != 0:
                break
            if y == 20:
                return x


print(smallest_multiple())
