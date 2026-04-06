class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.prefix = [[0]*len(matrix[0]) for i in range(len(matrix))]

        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[0])):
                if i == 0:
                    sum += matrix[i][j]
                    self.prefix[i][j]= sum
                else:
                    sum += matrix[i][j]
                    self.prefix[i][j]= sum + self.prefix[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.prefix[row2][col2]
        if row1 != 0:
            sum -= self.prefix[row1 -1][col2]
        
        if col1 != 0:
            sum -= self.prefix[row2][col1 -1]
        
        if row1 != 0 and col1 != 0:
            sum += self.prefix[row1 -1][col1 -1 ]
        
        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)