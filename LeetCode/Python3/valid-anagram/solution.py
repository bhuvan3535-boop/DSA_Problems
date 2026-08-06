class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in freq1:
                    freq1[s[i]] = 1
                else:
                    freq1[s[i]] += 1
                
                if t[i] not in freq2:
                    freq2[t[i]] = 1
                else:
                    freq2[t[i]] += 1
            if freq1 != freq2:
                return False
            else:
                return True