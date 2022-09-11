import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adjList = {i:[] for i in range(n)}
        
        # Step 1: Create edges
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
                
        # Step 2: Prim's algorithm
        
        res=0
        visit=set()
        minHeap=[[0,0]]
        
        while len(visit)<n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            
            for neiCost, nei in adjList[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
                    
        return res