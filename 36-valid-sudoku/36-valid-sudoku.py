class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            ele=[]
            for j in row:
                if j!=".":
                    if j in ele:
                        return False
                    else:
                        ele.append(j)
                        
        for j in range(len(board)):
            ele=[]
            for i in range(len(board)):
                if board[i][j]!=".":
                    if board[i][j] in ele:
                        return False
                    else:
                        ele.append(board[i][j])
                        
        for i in range(0,9,3):
            for j in range(0,9,3):
                ele=[]
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l]!=".":
                            if board[k][l] in ele:
                                return False
                            else:
                                ele.append(board[k][l])
                                
        return True