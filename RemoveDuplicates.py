class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Use two pointers approach
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1