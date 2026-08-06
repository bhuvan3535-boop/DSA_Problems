class Solution:
    def isAplanumeric(self, s):
        x = ord(s)
        if 48<=x<=57 or 97<=x<=122:
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        s =s.lower()
        j = len(s)-1
        i=0
        while i<j:
            if not self.isAplanumeric(s[i]):
                i += 1
            elif not self.isAplanumeric(s[j]):
                j -= 1
            
            elif s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False 
        
        return True