class Solution:
    def find132pattern(self, nums):
        stack = []
        s3 = float('-inf')
        
        # Traverse the array from right to left
        for i in range(len(nums) - 1, -1, -1):
            # If we find a number less than s3, we found a 132 pattern
            if nums[i] < s3:
                return True
            
            # Pop elements from the stack while the current number is greater than the top of the stack
            while stack and nums[i] > stack[-1]:
                s3 = stack.pop()  # Update s3 to the last popped value
            
            # Push the current number onto the stack
            stack.append(nums[i])
        
        return False