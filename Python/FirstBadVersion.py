def isBadVersion(version):
    """
    The API isBadVersion is defined for you.
    @param version, an integer
    @return a bool
    """
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left