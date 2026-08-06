class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        ans = 0
        while temp > 0:
            r = temp%10
            temp = temp//10
            ans = ans*10 + r
        if ans != x:
            return False
        else:
            return True

        