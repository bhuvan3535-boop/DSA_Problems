class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        n = len(nums)
        ans =[0]*n
        st1 = []
        
        for i in range(n-1, -1, -1):
            while len(st1)>0 and st1[-1]<=nums[i]:
                st1.pop()
            if len(st1)==0:
                ans[i] = -1
            else:
                ans[i] = st1[-1]
            st1.append(nums[i])
        
        return ans[:len(ans)//2]

        