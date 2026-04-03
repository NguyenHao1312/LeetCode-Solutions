class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Iterate backwards from the last digit
        for i in range(n - 1, -1, -1):
            # If the digit is less than 9, just add 1 and return immediately
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 (carry over the 1)
            digits[i] = 0
            
        # If the loop completes, it means all digits were 9 (e.g., 999 -> 000)
        # We need to prepend 1 to get the final result (1000)
        return [1] + digits