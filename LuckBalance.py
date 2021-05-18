def luckBalance(k, contests):
    c = 0
    contests.sort()
    contests = contests[::-1]
    imp = []
    nimp = []
    for i in contests:
        if 0 in i:
            nimp.append(i)
        else:
            imp.append(i)
    c = 0
    for i in range(len(imp)):
        if i < k:
            c = c+ imp[i][0]
        elif i>= k:
            c = c - imp[i][0]
    for i in range(len(nimp)):
        c = c + nimp[i][0]
    return(c)