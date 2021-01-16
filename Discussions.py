def plusMinus(arr):
    pos = []
    neg = []
    zer = []
    for i in arr:
        if i == 0:
            zer.append(i)
        elif i >0:
            pos.append(i)
        elif i < 0:
            neg.append(i)    
    n = len(neg)/len(arr)
    z = len(zer)/len(arr)
    p = len(pos)/len(arr)
    print('%.6f' % p)
    print('%.6f' % n)
    print('%.6f' % z)
