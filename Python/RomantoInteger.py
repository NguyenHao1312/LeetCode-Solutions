class Solution(object):
    def romanToInt(self, s):
        # Map of Roman symbols to their integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If the current value is less than the next value, 
            # it's a subtraction case (e.g., IV or IX).
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, just add the value.
                total += roman_map[s[i]]