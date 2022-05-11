def Special_Pythagorean_triplet():
    for c in range(500):
        for b in range(500):
            for a in range(500):
                if (a**2+b**2 == c**2) and (a+b+c==1000):
                    return (a*b*c)
print(Special_Pythagorean_triplet())