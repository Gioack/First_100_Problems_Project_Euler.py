def coin_sums():
    values = {x: 0 for x in range(201)}
    values[0] = 1
    available_coins = [1, 2, 5, 10, 20, 50, 100, 200]
    for coin in available_coins:
        for number in values:
            if number >= coin:
                values[number] += values[number-coin]
    return values[200]


print(coin_sums())
