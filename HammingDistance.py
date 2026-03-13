class Solution:
    def hammingDistance(self, x, y):
        # XOR the two numbers to find the differing bits
        xor = x ^ y
        
        # Count the number of 1s in the binary representation of xor
        distance = 0
        while xor:
            distance += xor & 1  # Increment distance if the last bit is 1
            xor >>= 1  # Right shift to check the next bit
        
        return distance