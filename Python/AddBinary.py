class Solution:
    def addBinary(self, a, b):
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_sum = carry
            if i >= 0:
                digit_sum += int(a[i])
                i -= 1
            if j >= 0:
                digit_sum += int(b[j])
                j -= 1

            result.append(str(digit_sum % 2))
            carry = digit_sum // 2

        return ''.join(reversed(result))