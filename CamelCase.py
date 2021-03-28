def camelcase(s):
    c = 0
    for i in s:
    	if i.isupper():
    		c+=1
    return c+1
print(camelcase("saveChangesInTheEditor"))
