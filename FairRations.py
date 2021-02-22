def fairRations(B):
    c = 0
    for i in range(len(B)-1):
        if B[i]%2!=0:
            c+=2
            B[i] = B[i]+1
            B[i+1] = B[i+1]+1
    if B[len(B)-1]%2 != 0:
        return("NO")
    else:
        return(c)