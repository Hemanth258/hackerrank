class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    # Add your code here
    def computeDifference(self):
        arr = []
        for i in self.__elements:
            for j in self.__elements:
                if i>j:
                    arr.append(i-j)
                else:
                    arr.append(j-i)
        self.maximumDifference = max(set(arr))
d = Difference([1,2,5])
d.computeDifference()
print(d.maximumDifference)