import urllib.request
def Open_file(url):
    return urllib.request.urlopen(url)
def Maximum_path_sum_I():
    triangle = Open_file("https://projecteuler.net/project/resources/p067_triangle.txt")
    Triangle_list = list()
    for line in triangle:
        line = line.strip()
        line = line.decode('utf-8')
        Triangle_list.append(line)
    Triangle_list = ([list(map(int, i.split())) for i in reversed(Triangle_list)])    
    for Index_line,line in enumerate(Triangle_list):
        if Index_line == 0:
            continue 
        for index_number, number in enumerate(line):
            Triangle_list[Index_line][index_number] += max(Triangle_list[Index_line-1][index_number],Triangle_list[Index_line-1][index_number+1])
    return Triangle_list[-1][0]
        
    
print(Maximum_path_sum_I())