def maximumToys(prices, k):
    prices.sort()
    c=0
    for i in prices:
        if k<i:
            pass
        else:
            k = k-i
            c+=1
    return c    
print(maximumToys([3, 7, 2, 9, 4],15))