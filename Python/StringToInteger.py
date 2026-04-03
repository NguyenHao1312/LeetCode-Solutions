class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        result *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result