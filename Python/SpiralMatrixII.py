class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        
        matrix = [[0] * n for _ in range(n)]
        num = 1
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            
            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix