def beautifulDays(i, j, k):
    count =0 
    for p in range(i,j+1):
        r = str(p)
        r = r[::-1]
        rev = int(r)
        c = (max(p,rev)-min(p,rev))/k
        c = str(c)
        if c[len(c)-1]=='0':
            count+=1
    return (count)