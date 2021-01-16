def compareTriplets(a, b):
    c = 0
    ac=0
    bc=0
    ar = [0]
    br = [0]
    for i in range(len(a)):
        if a[c]>b[c]:
            ac+=1
            ar.append(ac)
        elif a[c] == b[c]:
            pass
        else:
            bc+=1
            br.append(bc) 
        c+=1
    return (max(ar), max(br))
