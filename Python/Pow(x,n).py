class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        current_product = x
        
        while n > 0:
            if n % 2 == 1:  # If n is odd
                result *= current_product
            
            current_product *= current_product  # Square the base
            n //= 2  # Divide n by 2
        
        return result