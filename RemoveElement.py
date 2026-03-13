class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0

        # Use two pointers approach
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i