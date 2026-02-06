class Solution(object):
    def strStr(self, haystack, needle):
        # If needle is smaller than haystack, it can't be inside it
        if len(needle) > len(haystack):
            return -1
            
        # Iterate through the haystack
        # We only need to go up to index (len(haystack) - len(needle))
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of length 'needle' starting at 'i' matches
            if haystack[i : i + len(needle)] == needle:
                return i
                
        return -1