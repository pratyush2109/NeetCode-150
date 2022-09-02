class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        
        def bfs(r,c):
            queue = []
            queue.append((r,c))
            visited.add((r,c))
            tmp_area=1
            
            while queue:
                row, col = queue.pop(0)
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited:
                        tmp_area+=1
                        queue.append((r,c))
                        visited.add((r,c))
                        
            return tmp_area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    tmp_area=bfs(r,c)
                    max_area=max(max_area,tmp_area)
                    
        return max_area