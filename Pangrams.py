def pangrams(s):
    e = [chr(e) for e in range(97,123)]
    for i in s:
        i = i.lower()
        if i in e:
          c =  e.pop(e.index(i))
    if not e:
        return "pangram"
    else:
        return "not pangram"
print(pangrams("We promptly judged antique ivory buckles for the next prize"))