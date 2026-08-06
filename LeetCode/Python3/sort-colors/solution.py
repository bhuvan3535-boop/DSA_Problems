class Solution:
    def swap(self, nums, j, i):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        end = len(nums)-1
        i=0
        while i <= end:
            if nums[i]==0:
                self.swap(nums, start, i)
                start+=1
                i+=1
            elif nums[i] == 2:
                self.swap(nums, end, i)
                end-=1
            else:
                i+=1
        return nums

