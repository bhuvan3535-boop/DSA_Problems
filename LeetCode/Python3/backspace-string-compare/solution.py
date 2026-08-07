class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []
        for ch in list(s):
            if ch != '#':
                st1.append(ch)
            elif len(st1)>0:
                st1.pop()
        for ch in list(t):
            if ch != '#':
                st2.append(ch)
            elif len(st2)>0:
                st2.pop()
        return st1==st2
            


        