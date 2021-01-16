def merge_the_tools(string, k):
    dev = len(string)/k
    c = 0
    for i in range(1,len(string)+1):
        if i%k == 0:
            s = string[c:i]
            mylist = list(dict.fromkeys(s))
            print("".join(mylist))
            c = i