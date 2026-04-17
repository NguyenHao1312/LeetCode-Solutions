class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        
        # Create a 2D array to store the number of paths to each cell
        dp = [[0] * n for _ in range(m)]
        
        # There is only one way to reach any cell in the first row or first column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the dp array using the relation: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]