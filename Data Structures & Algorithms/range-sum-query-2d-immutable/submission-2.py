class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) + 1
        n = len(matrix[0]) + 1
        prefix = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + matrix[i][j] 
        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row2+1][col1] - self.prefix[row1][col2+1] + self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)