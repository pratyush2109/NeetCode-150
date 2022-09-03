class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        queue=[]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    queue.append((r,c))
                
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue and fresh>0:
            for i in range(len(queue)):
                r, c =queue.pop(0)
                for dr,dc in directions:
                    row, col=r+dr,c+dc
                    if row not in range(rows) or col not in range(cols) or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    queue.append((row,col))
                    fresh-=1
            time+=1

        if fresh==0:
            return time
        return -1