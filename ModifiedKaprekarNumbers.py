def kaprekarNumbers(p, q):
    arr = []
    for i in range(p,q+1):
        sq = i*i
        sq = str(sq)
        if int(sq) > 9:
            l = sq[:len(sq)//2]
            r = sq[len(sq)//2:]
            if (int(l)+int(r)) == i:
                arr.append(i)    
        else:
            sq = i*i
            if i == sq:
                arr.append(i)
    if not arr:
        print("INVALID RANGE")
    else:
        print(*arr)