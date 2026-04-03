class Solution:
    def findContentChildren(self, g, s):
        # Sort the greed factors and cookie sizes
        g.sort()
        s.sort()
        
        content_children = 0
        cookie_index = 0
        
        # Iterate through each child and try to find a cookie for them
        for greed in g:
            while cookie_index < len(s) and s[cookie_index] < greed:
                cookie_index += 1
            
            if cookie_index < len(s):
                content_children += 1
                cookie_index += 1  # Move to the next cookie for the next child
        
        return content_children