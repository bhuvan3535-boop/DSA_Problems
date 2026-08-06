class Solution:
    def sortString(self, s):
        s=list(s)
        s.sort()
        return "".join(s)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for s in strs:
            key = self.sortString(s)
            if key in freq:
                freq[key].append(s)
            else:
                freq[key] = [s]
        return list(freq.values())