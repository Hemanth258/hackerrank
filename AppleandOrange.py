def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_house = 0
    for i in apples:
        if (a+i) in range(s,t+1):
            a_house+=1 
    o_house = 0
    for j in oranges:
        if (b+j) in range(s,t+1):
            o_house+=1        
    print(a_house)
    print(o_house)
    