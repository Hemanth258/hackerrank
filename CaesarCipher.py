def caesarCipher(s, k):
    sapl = [chr(i) for i in range(97,123)]
    uapl = [chr(i).upper() for i in range(97,123)]
    f = []
    for i in s:
        if i in sapl:
            if sapl.index(i)+k<len(sapl):
                f.append(sapl[sapl.index(i)+k])
            elif sapl.index(i)+k>=len(sapl):
                while True:
                    if sapl.index(i)+k-26 < len(sapl):
                        f.append(sapl[sapl.index(i)+k-26])
                        break
                    k = k - 26
        elif i in uapl:
            if uapl.index(i)+k<len(uapl):
                f.append(uapl[uapl.index(i)+k])
            elif uapl.index(i)+k>=len(uapl):
                while True:
                    if uapl.index(i)+k-26 < len(uapl):
                        f.append(uapl[uapl.index(i)+k-26])
                        break
                    k = k - 26
        else:
            f.append(i)
    return("".join(f))