import urllib.request


def open_file(url):
    return urllib.request.urlopen(url).read().decode("utf-8")


def get_score(name):
    alphabeth = {letter:lenght for letter,lenght in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(1,27))}
    total_name = 0
    for letter in name:
        total_name += alphabeth[letter]
    return total_name


def arrange_string(names):
    names = names.replace('"',"")
    names = names.split(",")
    names = sorted(names)
    return names


def get_score_of_each_name(names):
    total = 0
    for index,name in zip(range(1,len(names)+2),names):
        total_name = get_score(name)
        total += (index*total_name)   
    return total


def names_scores():
    names = open_file("https://projecteuler.net/project/resources/p022_names.txt")
    names = arrange_string(names)
    return get_score_of_each_name(names)
     


print(names_scores())