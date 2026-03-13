class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            slow, fast = i, i
            
            # Determine the direction of movement
            direction = nums[i] > 0
            
            while True:
                # Move slow pointer one step
                slow = (slow + nums[slow]) % n
                # Move fast pointer two steps
                fast = (fast + nums[fast]) % n
                fast = (fast + nums[fast]) % n
                
                # Check if we found a cycle
                if slow == fast:
                    # Check if the cycle is valid (length > 1 and same direction)
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True
                
                # Check if the movement direction is consistent
                if (nums[slow] > 0) != direction or (nums[fast] > 0) != direction:
                    break
            
            # Mark all elements in the current path as visited
            j = i
            while nums[j] != 0:
                next_index = (j + nums[j]) % n
                nums[j] = 0  # Mark as visited
                j = next_index
        
        return False