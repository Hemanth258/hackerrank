def birthdayCakeCandles(candles):
    m = max(candles)
    c = 0
    for i in candles:
        if i == m:
            c+=1
    return c