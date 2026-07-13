class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        max_area = 0
        def dfs(r, c, total):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            total += 1
            grid[r][c] = 0

            for dr, dc in directions:
                total += dfs(r + dr, c + dc, 0)
            
            return total

        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))
        
        return max_area

