class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * COLS for _ in range(ROWS)]
        
        for i in range(ROWS):
            for j in range(COLS):
                top = self.sum_matrix[i-1][j] if i > 0 else 0
                left = self.sum_matrix[i][j-1] if j > 0 else 0
                diagonal = self.sum_matrix[i-1][j-1] if i > 0 and j > 0 else 0
                
                self.sum_matrix[i][j] = matrix[i][j] + top + left - diagonal

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.sum_matrix[row2][col2]
        above = self.sum_matrix[row1-1][col2] if row1 > 0 else 0
        left = self.sum_matrix[row2][col1-1] if col1 > 0 else 0
        top_left = self.sum_matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        
        return total - above - left + top_left