class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If we've seen this character AND it's inside our current window
            if char in seen and seen[char] >= left:
                # Move the left pointer to the right of the old duplicate
                left = seen[char] + 1
            
            # Update the character's latest index
            seen[char] = right
            
            # Calculate the window size and update max_length
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)
            
        return max_length