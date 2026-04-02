class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matriz_row = [[0] * 9 for _ in range(9)]
        matriz_col = [[0] * 9 for _ in range(9)]
        matriz_box = [[0] * 9 for _ in range(9)]
        count_box_h = 0
        #row
        for row in range(9):
            if row % 3 == 0 and row !=0:
                count_box_h += 3
            for col in range(9):
                if board[row][col] != '.':
                    count_box_l = 0
                    if col > 2:
                        count_box_l = 1
                        if col > 5:
                            count_box_l = 2

                    matriz_row[row][int(board[row][col]) -1] += 1
                    matriz_col[col][int(board[row][col]) -1] += 1
                    matriz_box[count_box_l + count_box_h][int(board[row][col]) -1] += 1
                    if matriz_row[row][int(board[row][col]) -1] > 1 or matriz_col[col][int(board[row][col])-1] > 1 or matriz_box[count_box_l + count_box_h][int(board[row][col])-1] >1:
                        print(matriz_row)
                        print(matriz_col)
                        print(matriz_box)
                        return False

        return True
