class Solution:
    def lowerBound(self, nums, target, n):
        l = 0
        r = n-1
        flag = n
        while l<=r:
            mid = (l+r)//2
            if nums[mid] >= target:
                flag = mid
                r = mid-1
            else:
                l = mid+1
        return flag
    
    def upperBound(self, nums, target, n):
        l = 0
        r = n-1
        flag = n
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > target:
                flag = mid
                r = mid-1
            else:
                l = mid+1
        return flag
            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lb = self.lowerBound(nums, target, n)
        ub = self.upperBound(nums, target, n)
        if lb == ub:
            return [-1, -1]
        else:
            return [lb, ub-1]

            
