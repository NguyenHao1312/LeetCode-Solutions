class Solution(object):
    def sortArray(self, nums):
        # Base case: A list of 0 or 1 elements is already sorted
        if len(nums) <= 1:
            return nums
        
        # Divide: Split the array into two halves
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # Conquer: Merge the sorted halves
        return self.merge(left_half, right_half)
    
    def merge(self, left, right):
        sorted_list = []
        i = j = 0
        
        # Compare elements from both lists and append the smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        
        # Append any remaining elements (one of these will be empty)
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list
        