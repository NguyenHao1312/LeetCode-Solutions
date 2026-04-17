class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = float('-inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num
        return third if third != float('-inf') else first