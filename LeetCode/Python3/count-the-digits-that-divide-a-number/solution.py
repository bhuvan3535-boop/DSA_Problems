class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        c = 0
        while num > 0:
            r = num % 10
            num = num // 10
            if(temp%r == 0):
                c += 1
        return c