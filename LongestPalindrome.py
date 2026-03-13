class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
            
        start = 0
        max_len = 0
        
        def expandAroundCenter(left, right) :
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome we just found
            return right - left - 1
            
        for i in range(len(s)):
            # Check for odd-length palindromes (single character center)
            len1 = expandAroundCenter(i, i)
            # Check for even-length palindromes (center is between two characters)
            len2 = expandAroundCenter(i, i + 1)
            
            # Find the max length from both checks
            curr_max = max(len1, len2)
            
            # If we found a longer palindrome, update our tracking variables
            if curr_max > max_len:
                max_len = curr_max
                # Calculate the starting index of this new longest palindrome
                start = i - (curr_max - 1) // 2
                
        return s[start : start + max_len]