from urllib.request import urlopen


def passcode_derivation():
    digits_strengths = {str(x): set() for x in range(0, 10)}
    # Since 4 and 5 never appear we delete them
    digits_strengths.pop("4")
    digits_strengths.pop("5")
    text = read_online_file(
        "https://projecteuler.net/project/resources/p079_keylog.txt")
    for access in text:
        digits_strengths[access[0]] = digits_strengths[access[0]].union(
            {access[1], access[2]})
        digits_strengths[access[1]].add(access[2])
    digits_descending_order_by_strength = sorted(digits_strengths, key=lambda x: len(
        digits_strengths[x]), reverse=True)
    return "".join(digits_descending_order_by_strength)


def read_online_file(url):
    text = urlopen(url)
    text = str(text.read(), 'utf-8').rstrip()
    text = text.split("\n")
    return text


if __name__ == "__main__":
    print(passcode_derivation())
