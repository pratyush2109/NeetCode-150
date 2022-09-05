class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        islands=0
        visited=set()
        
        def bfs(r,c):
            queue=[]
            visited.add((r,c))
            queue.append((r,c))
            
            while queue:
                row,col=queue.pop(0)
                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]=="1":
                        queue.append((r,c))
                        visited.add((r,c))
                        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1
                    
        return islands