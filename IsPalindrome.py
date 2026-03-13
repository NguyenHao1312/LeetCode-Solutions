class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Single digit numbers are palindromes
        if x < 10:
            return True

        # Convert the number to a string and check if it reads the same forwards and backwards
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True