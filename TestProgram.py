from random import randint

def arraySort(n):
    arrays = []
    length = []
    for i in range(n):
        p = randint(1,15)
        mass = []

        if p not in length:    
            for i in range(p):
                n = randint(-15,15)
                mass.append(n)
            length.append(p)
            arrays.append(mass)
        else: 
            while p in length:
                p = randint(1,15)
            for i in range(p):
                n = randint(-15,15)
                mass.append(n)
            length.append(p)
            arrays.append(mass)

    sortedArrays = [] 
    for i in arrays:
        if arrays.index(i) % 2 == 0:
            i = sorted(i)
            sortedArrays.append(i)
        else:
            i = sorted(i, reverse = True)
            sortedArrays.append(i)
    return sortedArrays

