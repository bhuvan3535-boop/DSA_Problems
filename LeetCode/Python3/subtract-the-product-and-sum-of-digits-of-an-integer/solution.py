class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        prod = 1
        temp = n
        while(temp > 0):
            r = temp%10
            temp = temp//10
            summ = summ + r
            prod = prod*r
        return prod - summ