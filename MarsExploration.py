def marsExploration(s):
    c = 0
    for i in range(len(s)):
        i = i*3
        f = s[i:i+3]
        if f[0] != 'S':
            c+=1
        if f[1] != 'O':
            c+=1
        if f[2] != 'S':
            c+=1
        if i+3== len(s):
            break
    return c

print(marsExploration("SOSTOT"))