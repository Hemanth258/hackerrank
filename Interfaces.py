class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        arr = []
        for i in range(n+1):
            for j in range(n+1):
                if i*j == n:
                    arr.append(i)
        return sum(arr)