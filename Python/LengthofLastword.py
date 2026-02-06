class Solution:
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0
        return len(words[-1])