def birthday(s, d, m):
        c=0
        for i in range(len(s)-m+1):
            su = sum(s[i:i+m])
            if su == d:
                c+=1
        return c
                  