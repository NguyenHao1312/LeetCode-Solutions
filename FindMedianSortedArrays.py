class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # We always want to binary search on the smaller array for efficiency.
        # This keeps the time complexity at strictly O(log(min(m, n))).
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partitioning both arrays
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Find the boundary values, using infinity for edge cases out of bounds
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we have found the perfect partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If the combined length is odd, the median is the max of the left side
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # If even, it's the average of the max left and min right
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                    
            # If our partition in nums1 is too far right, move the search space left
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            # If our partition in nums1 is too far left, move the search space right
            else:
                left = partition1 + 1