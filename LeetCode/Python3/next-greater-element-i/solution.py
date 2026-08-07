class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        ans = {}
        st1 = []

        for i in range(n-1, -1,-1):
            while len(st1)>0 and st1[-1]<=nums2[i]:
                st1.pop()
            if len(st1)==0:
                ans[nums2[i]] = -1
            else:
                ans[nums2[i]] = st1[-1]
            
            st1.append(nums2[i])

        res = []
        for i in nums1:
            res.append(ans[i])
        return res
        