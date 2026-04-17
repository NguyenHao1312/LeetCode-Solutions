class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-', '').upper()
        result = []
        for i in range(len(s) - 1, -1, -k):
            result.append(s[max(0, i - k + 1):i + 1])
        return '-'.join(result[::-1])