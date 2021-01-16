def viralAdvertising(n):
    s = [5]
    l = [2]
    c = [2]
    cum = [2]
    for i in range(0,n):
        com = s[i]//2
        c.append(com)
        sh = com*3
        s.append(sh)
        lk = sh//2
        l.append(lk)
        cum.append(lk+cum[i])
    return(cum[n-1])