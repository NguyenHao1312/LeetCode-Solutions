class Solution(object):
    def pivotIndex(self, nums):
        # Calculate the total sum of the array once
        total_sum = sum(nums)
        left_sum = 0
        
        for i, val in enumerate(nums):
            # The right sum is the total minus the left sum and the current element
            # We want to find where left_sum == right_sum
            if left_sum == (total_sum - left_sum - val):
                return i
            
            # Add current value to left_sum for the next iteration
            left_sum += val
            
        return -1