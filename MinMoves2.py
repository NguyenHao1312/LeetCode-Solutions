class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        n = len(nums)
        median = nums[n // 2]  # Get the median element
        moves = 0
        
        # Calculate the total moves required to make all elements equal to the median
        for num in nums:
            moves += abs(num - median)
        
        return moves