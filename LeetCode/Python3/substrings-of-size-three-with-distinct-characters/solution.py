class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        freq = set()
        count = 0
        for i in range(0,len(s)-2):
            j = i+1
            k = i+2

            freq.add(s[i])
            freq.add(s[j])
            freq.add(s[k])
            if len(freq) == 3:
                count = count+1
            freq.clear()
        return count
