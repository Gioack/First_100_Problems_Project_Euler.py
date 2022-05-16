def count_letter(num):
    number_of_Letter = 0
    num = str(num)
    units_letter_count = {"1":3, "2":3,"3":5,"4":4,"5":4,"6":3,"7":5,"8":5,"9":4,"0":0}
    tens_letter_count = {"1":3, "2":6,"3":6,"4":5,"5":5,"6":5,"7":7,"8":6,"9":6,"0":0}
    count_exceptions = {"10":3,"11":6,"12":6,"13":8,"14":8,"15":7,"16":7,"17":9,"18":8,"19":8}
    
    if len(num) == 1:
        number_of_Letter += units_letter_count[num]
    
    if len(num) == 2:
        if num[0] != "1":
            number_of_Letter += units_letter_count[num[1]]
            number_of_Letter += tens_letter_count[num[0]]
        else:
            number_of_Letter += count_exceptions[num]
    
    if len(num) == 3: 
        if (num[2] != "0") or (num[1] != "0"): 
            number_of_Letter += units_letter_count[num[0]]+10 
        else:
            number_of_Letter += units_letter_count[num[0]]+7
        if num[1] != "1":
            number_of_Letter += tens_letter_count[num[1]] 
            number_of_Letter += units_letter_count[num[2]]     
        else:
            number_of_Letter += count_exceptions[num[1:]]
    
    return number_of_Letter


def number_letter_counts():
    counter = 11 # it's not 0 because we count manually one thousand
    for x in range(1,1000):
        counter += count_letter(x)
    return counter


print(number_letter_counts())