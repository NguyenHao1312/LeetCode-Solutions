class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()  # Sort the array to handle duplicates
        self.backtrack(nums, [], result)
        return result
    def backtrack(self, nums, path, result):
        if not nums:
            result.append(path)
            return

        for i in range(len(nums)):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], result)