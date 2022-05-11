def Count_Letter(num):
    Number_of_Letter = 0
    Units_letter_count = {"1":3, "2":3,"3":5,"4":4,"5":4,"6":3,"7":5,"8":5,"9":4,"0":0}
    Tens_letter_count = {"1":3, "2":6,"3":6,"4":5,"5":5,"6":5,"7":7,"8":6,"9":6,"0":0}
    Unit_letter_count_exceptions = {"10":3,"11":6,"12":6,"13":8,"14":8,"15":7,"16":7,"17":9,"18":8,"19":8}
    num = str(num)
    if len(num) == 1:
        Number_of_Letter += Units_letter_count[num]
    if len(num) == 2:
        if num[0] == "1":
            Number_of_Letter += Unit_letter_count_exceptions[num]
        else:
            Number_of_Letter += Units_letter_count[num[1]]
            Number_of_Letter += Tens_letter_count[num[0]]
    if len(num) == 3:
        if (num[2] == "0") and (num[1]=="0"):
            Number_of_Letter += Units_letter_count[num[0]] + 7
        else:
            Number_of_Letter += Units_letter_count[num[0]] + 10 #+13
        if num[1] == "1":
            Number_of_Letter += Unit_letter_count_exceptions[num[1:]]
        else:
            Number_of_Letter += Tens_letter_count[num[1]] #+5
            Number_of_Letter += Units_letter_count[num[2]] #+5
    return Number_of_Letter

def Number_letter_counts():
    counter = 11
    for x in range(1,1000):
        counter += Count_Letter(x)
    return counter

print(Number_letter_counts())