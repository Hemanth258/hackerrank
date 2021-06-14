def minimumLoss(price):
    arr = price
    price = sorted(price)
    price = price[::-1]
    m = max(price)
    f = []
    for i in range(1,len(price)):
        if price[i-1] - price[i]<m and arr.index(price[i])>arr.index(price[i-1]):
            m = price[i-1] - price[i]
    return (m)

print(minimumLoss([5,10,3]))