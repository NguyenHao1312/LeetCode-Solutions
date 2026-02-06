class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        
        # Loop 1: Pick the first number (index i)
        for i in range(n):
            
            # Loop 2: Pick the second number (index j)
            # Start from i + 1 so we don't use the same number twice
            for j in range(i + 1, n):
                
                # Check if they add up to target
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # Return an empty list if no solution is found
# Example usage:
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]