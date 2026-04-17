class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Edge case: If either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array to hold the intermediate sums
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both numbers to facilitate multiplication from least significant digit
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Multiply each digit of num1 with each digit of num2
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit_product = int(num1[i]) * int(num2[j])
                result[i + j] += digit_product
                result[i + j + 1] += result[i + j] // 10  # Carry over
                result[i + j] %= 10  # Keep only the last digit
        
        # Remove leading zeros and reverse back to get the final product
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return ''.join(map(str, result[::-1]))