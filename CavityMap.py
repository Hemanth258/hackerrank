def cavityMap(g):
    if len(g) == 1:
        return(g)
    else:
        con = []
        for i in range(1,len(g)-1):
            for j in range(1,len(g)-1):
                if g[i][j]>g[i-1][j]:
                    if g[i][j]>g[i][j-1]:
                        if g[i][j]>g[i][j+1]:
                            if g[i][j]>g[i+1][j]:
                                con.append([i,j])
        for i,j in con:
            c=list(g[i])
            c[j] = 'X'
            g[i] = "".join(c)

        for i in g:
            return g
    