class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        
        for n in nums:
            if n == 1:
                # Increment current streak
                current_count += 1
                # Update max immediately to handle cases ending with 1
                max_count = max(max_count, current_count)
            else:
                # Reset streak when we hit a 0
                current_count = 0
                
        return max_count