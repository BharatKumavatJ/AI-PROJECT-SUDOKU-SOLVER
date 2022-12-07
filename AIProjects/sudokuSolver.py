class Sudoku:
    
    def __init__(self, itt):
        self.itt = itt
    def recur(self, i, j, board, row, col, mat):
        
        if (j == 9 and i == 8):
            
            if ( self.itt == 1) :
                exit()
            print("\n-----------Sudoku ------")

            for k in range(0, 9):
                for l in range(0, 9):
                    print(board[k][l] , end = " ")
                print("\n-----------------")
            self.itt = self.itt + 1

            return
            
        if (j == 9):
            i = i + 1
            j = 0
        if(board[i][j] != '.'):
            self.recur(i, j  + 1, board, row, col, mat)
        else :
            for num in range(1, 10):
                if(((row[i] & (1 << num)) == 0) and ((col[j] & (1 << num)) == 0)  and (mat[((i // 3) * 3) + (j // 3)] & (1 << num)) == 0):
                    board[i][j] = str(num) 
                    val = num
                    row[i] = row[i]  ^ (1 << (val))
                    col[j] = col[j]  ^ (1 << (val))
                    mat[(i // 3 ) * 3 + (j // 3)] = mat[(i // 3 ) * 3 + (j // 3)] ^  (1 << (val))

                    self.recur(i, j  + 1, board, row, col, mat)

                    
                    
                    board[i][j] = '.'
                    row[i] = row[i]  ^ (1 << (val))
                    col[j] = col[j]  ^ (1 << (val))
                    mat[(i // 3 ) * 3 + (j // 3)]  = mat[(i // 3 ) * 3 + (j // 3)] ^  (1 << (val))
        
    def solveSudoku(self, board):
        row = [0] * 9
        col = [0] * 9
        mat = [0] * 9
        
        for i in range(0, 9):
            for j in range(0, 9):
                if(board[i][j] != '.'):
                    val = int(board[i][j])
                    row[i] = row[i]  ^ (1 << val)
                    col[j] = col[j]  ^ (1 << val)
                    mat[(i // 3 ) * 3 + (j // 3)]  = mat[(i // 3 ) * 3 + (j // 3)] ^  (1 << val)
        self.recur(0, 0, board, row, col, mat)
    
board = [[".",".",".",".","7",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solve = Sudoku(0)
solve.solveSudoku(board)

