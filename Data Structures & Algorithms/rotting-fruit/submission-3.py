from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque([])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))
        max_mins = 0
        while queue:
            r, c, mins = queue.popleft()
            max_mins = max(max_mins, mins)
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                    continue
                num_fresh -= 1
                queue.append((nr, nc, mins + 1))
                grid[nr][nc] = 2
                


        

        return max_mins if num_fresh == 0 else -1

        
        

        