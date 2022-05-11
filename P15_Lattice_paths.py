def Summation(num):
    Summation = 1
    for i in range(1,num+1):
        Summation *= i
    return Summation
def Lattice_paths(): 
    return Summation(40)/(Summation(20)*Summation(20))

print(Lattice_paths())

