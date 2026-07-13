class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return
            
            # This cell is an O
            board[r][c] = 'R'

            for dr, dc in directions:
                dfs(r + dr, c + dc)
            

        # First column
        for r in range(0,ROWS):
            dfs(r, 0)
        
        # First row
        for c in range(0, COLS):
            dfs(0, c)
        
        # Last column
        for r in range(ROWS):
            dfs(r, COLS - 1)
        
        # Last row
        for c in range(COLS):
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'R':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        