class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        k = len(nums1) - 1
        while k>=0:
            if i<0:
                nums1[k]=nums2[j]
                j-=1
                k-=1
            elif j<0:
                nums1[k] = nums1[i]
                i-=1
                k-=1
            elif nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i-=1
                k-=1
            else:
                nums1[k]=nums2[j]
                j-=1
                k-=1

        