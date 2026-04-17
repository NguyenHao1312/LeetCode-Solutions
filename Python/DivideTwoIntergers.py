class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if divisor == 0:
            return 2**31 - 1
        sign = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += multiple
                temp <<= 1
                multiple <<= 1
        return min(quotient if sign else -quotient, 2**31 - 1)