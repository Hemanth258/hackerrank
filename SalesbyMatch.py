def sockMerchant(n, ar):
    d = dict(Counter(ar))
    e = 0
    o = 0
    print(d)
    for i,k in d.items():
        if k > 1 and k%2 == 0:
            e = k+e
        elif k > 1 :
            o =(k-1)+o
    return ((e//2)+ (o//2))