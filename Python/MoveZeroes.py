class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        """
        last_non_zero_found_at = 0
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1