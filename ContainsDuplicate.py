class Solution:
    def containsDuplicate(self, nums):
        # Create a hash set to store elements we have seen
        seen = set()
        
        for num in nums:
            # If the number is already in the set, we found a duplicate
            if num in seen:
                return True
            # Otherwise, add it to the set
            seen.add(num)
            
        # If we finish the loop, no duplicates were found
        return False