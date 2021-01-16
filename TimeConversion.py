def timeConversion(s):
    f = s[0:2]
    l = s[len(s)-2:len(s)]
    if f == '12' and l =='AM':
        return('00'+s[2:len(s)-2])
    elif f != '12' and l == 'PM':
        f = int(f)
        conv = f+12
        return(str(conv)+s[2:len(s)-2])
    else:
        return(s[0:len(s)-2])