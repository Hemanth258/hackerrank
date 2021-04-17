def funnyString(s):
    s2 = s[::-1]
    a1 = []
    a2 = []
    for i in range(1,len(s)):
        a1.append(max(ord(s[i]), ord(s[i-1]))- min(ord(s[i]), ord(s[i-1])))
        a2.append(max(ord(s2[i]), ord(s2[i-1]))- min(ord(s2[i]), ord(s2[i-1])))
    if a1 == a2:
        return "Funny"
    else:
        return "Not Funny"

print(funnyString("lmnop"))