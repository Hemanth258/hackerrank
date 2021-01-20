def libraryFine(d1, m1, y1, d2, m2, y2):
    if y2==y1:
        if m2>m1:
            return(0)
        elif m2<m1:
            return(500*(max(m1,m2)-min(m1,m2)))
        else:
            if d2<=d1:
                return(15*(max(d1,d2)-min(d1,d2)))
            else:
                return(0)
    elif y2>y1:
        return(0)            
    else:
        return(10000*(max(y1,y2)-min(y1,y2)))