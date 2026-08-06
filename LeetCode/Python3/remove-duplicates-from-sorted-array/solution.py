class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        key = nums[0]
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                temp = nums[i]
                nums[i]=nums[j+1]
                nums[j+1] = temp
                j+=1
        return j+1