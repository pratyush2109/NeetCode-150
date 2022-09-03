class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols=len(board), len(board[0])
        
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or board[r][c]!="O":
                return
            
            board[r][c]="T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        #Step 1: Capture the unsurrounded region (O->T)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and r in [0,rows-1] or c in [0,cols-1]:
                    dfs(r,c)
        
        #Step 2: Capture surrounded region (O->X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
        
        #Step 3: Uncapture surrounded region (T->O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"