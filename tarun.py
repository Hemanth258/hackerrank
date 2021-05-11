n = int(input())
s = input()
def james(n,s):
    m = map(list,s)
    m = list(s)
    f = ['O']*len(s)
    for i in range(len(s)):
        if i == 0 and m[i] == 'c':
            f[i] = 'I'
            if i+1 <= len(s):
                f[i+1] = 'I'
            if i+2 <= len(s):
                f[i+2] = 'I'
        elif i == 1 and m[i] == 'c':
            f[i] = 'I'
            f[i-1] = 'I'
            if i+1 <= len(s):
                f[i+1] = 'I'
            if i+2 <= len(s):
                f[i+2] = 'I'
        else:
            if m[i] == 'c':
                f[i] = 'I'
                f[i-1] = 'I'
                f[i-2] = 'I'
                if i+1<len(s):
                    f[i+1] = 'I'
                if i+2<len(s):
                    f[i+2] = 'I'
        if m[i] == 'n' and m[i-1] != 'c' and m[i-2]!='c':
            f[i] = 'U'
    return "".join(f)
#print(james(n,s))
james(n,s)
