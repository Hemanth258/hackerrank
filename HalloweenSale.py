def howManyGames(p, d, m, s):
    c = 0
    f = [p]
    while(True):
        p-=d
        f.append(p)
        if p <= m:
            break
    if f[len(f)-1] != m:
        f[len(f)-1] = m
    su = 0
    for i in f:
        su+=i
        if su >=s:
            break
        else:
            c+=1
    ar = []
    if su >= s:
        return(c)
    else:
        while(su<=s):
            ar.append(c)
            su+=m
            c+=1
    if not ar:
        return 0
    else:
        return(max(ar))