class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reversed_x = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before updating reversed_x
            if reversed_x > (INT_MAX - digit) // 10:
                return 0
            
            reversed_x = reversed_x * 10 + digit
        
        result = sign * reversed_x
        return result if INT_MIN <= result <= INT_MAX else 0