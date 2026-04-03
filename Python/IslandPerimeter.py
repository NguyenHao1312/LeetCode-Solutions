class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # If it's land
                    perimeter += 4  # Start with 4 sides
                    
                    # Check the upper cell
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2  # Remove the shared edge
                    
                    # Check the left cell
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2  # Remove the shared edge
        
        return perimeter