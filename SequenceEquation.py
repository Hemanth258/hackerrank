def permutationEquation(p):
    c=0
    arr = []
    for i in range(1,len(p)+1):
        c = (p.index(i)+1)
        arr.append(p.index(c)+1)
    return arr