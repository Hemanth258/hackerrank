n = int(input())
s = input()
def james(n,s):
    f = ['O']*len(s)
    for i in range(len(s)):
        if i == 0 and s[i] == 'c':
            f[i] = 'I'
            if i+1 <= len(s):
                f[i+1] = 'I'
            if i+2 <= len(s):
                f[i+2] = 'I'
        elif i == 1 and s[i] == 'c':
            f[i] = 'I'
            f[i-1] = 'I'
            if i+1 <= len(s):
                f[i+1] = 'I'
            if i+2 <= len(s):
                f[i+2] = 'I'
        else:
            if s[i] == 'c':
                f[i] = 'I'
                f[i-1] = 'I'
                f[i-2] = 'I'
                if i+1<len(s):
                    f[i+1] = 'I'
                if i+2<len(s):
                    f[i+2] = 'I'
        if s[i] == 'n' and s[i-1] != 'c' and s[i-2]!='c':
            f[i] = 'U'
    return "".join(f)
#print(james(n,s))
james(n,s)
