import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        
        minHeap=[[grid[0][0],0,0]]
        visit.add((0,0))
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            
            if r==n-1 and c==n-1:
                return t
            for dr,dc in directions:
                neiR, neiC=r+dr,c+dc
                if neiR<0 or neiC<0 or neiR==n or neiC==n or (neiR,neiC) in visit:
                    continue
                visit.add((neiR,neiC))
                heapq.heappush(minHeap, [max(t,grid[neiR][neiC]), neiR, neiC])