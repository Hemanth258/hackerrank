def findDigits(n):
    c = 0
    s = str(n)
    for i in s:
        i = int(i)
        if i != 0:
            d = n/i
            d = str(d)
            if d[len(d)-1] == '0':
                c+=1
    return c