def timeInWords(h, m):
    a =  ["zero", "one", "two", "three", "four", "five", 
"six", "seven", "eight", "nine", "ten", "eleven", "twelve",
"thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
"eighteen", "nineteen", "twenty", "twenty one", "twenty two",
"twenty three", "twenty four", "twenty five", "twenty six", 
"twenty seven", "twenty eight", "twenty nine"]
    if m == 00:
        return(a[h]+" o' clock")
    elif m <= 9:
        return(a[m]+" minute"+" past "+a[h])
    elif m == 15:
        return("quarter past "+a[h])
    elif m<30 and m!=15:
        return(a[m]+" minutes past "+a[h])
    elif m == 30:
        return("half past "+a[h])
    elif m > 30 and m!=45:
        return(a[60-m]+" minutes to "+a[h+1])
    elif m == 45:
        return("quarter to "+a[h+1])
print(timeInWords(10,57))