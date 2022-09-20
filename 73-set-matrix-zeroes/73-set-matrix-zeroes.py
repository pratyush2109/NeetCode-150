class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows=set()
        zero_cols=set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    zero_rows.add(i)
                    zero_cols.add(j)
                    
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j]=0
                
        for i in range(rows):
            for j in zero_cols:
                matrix[i][j]=0