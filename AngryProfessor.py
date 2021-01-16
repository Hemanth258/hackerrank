def angryProfessor(k, a):
    f = 0
    l = 0
    for i in a:
        if i<=0:
            f+=1
        elif i>0:
            l+=1
    if f>=k:
        return("NO")
    else:
        return("YES")