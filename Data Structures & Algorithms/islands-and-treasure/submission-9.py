from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        LAND = 2147483647
        q = deque([])
        # Add all treasure chests to the queue
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        while q:
            r, c, dist = q.popleft()
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                nr = r + dr
                nc = c + dc
                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != LAND:
                    continue
                
                q.append((nr, nc, dist + 1))
                grid[nr][nc] = dist + 1
            

