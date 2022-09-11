import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList={i:[] for i in range(n+1)}
        for i in range(len(times)):
            u,v,w=times[i]
            adjList[u].append([w, v])
            
        minHeap=[[0,k]]
        cost=0
        visit=set()
        
        while len(visit)<n and minHeap:
            dist, j=heapq.heappop(minHeap)
            cost=max(dist,cost)
            visit.add(j)
            
            for neiCost, nei in adjList[j]:
                if nei not in visit:
                    heapq.heappush(minHeap, [cost+neiCost, nei])
                    
        if len(visit)!=n:
            return -1
        return cost