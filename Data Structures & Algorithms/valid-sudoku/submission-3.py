class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        grid_map = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] in row_map[r] or board[r][c] in col_map[c] or board[r][c] in grid_map[(r // 3, c // 3)]:
                        return False
                    
                    row_map[r].add(board[r][c])
                    col_map[c].add(board[r][c])
                    grid_map[(r // 3, c // 3)].add(board[r][c])
        
        return True

