class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        hex_digits = "0123456789abcdef"
        result = ""
        for _ in range(8):
            result = hex_digits[num & 0xf] + result
            num >>= 4
        return result.lstrip("0")