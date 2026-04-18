class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = list(sorted(nums1 + nums2))
        len_nums = len(nums)

        if len_nums % 2:
            return nums[len_nums // 2]
        else:
            return (nums[len_nums // 2 - 1] + nums[len_nums // 2]) / 2