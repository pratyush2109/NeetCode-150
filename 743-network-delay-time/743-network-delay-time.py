class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [[float('inf') for j in range(n+1)] for i in range(n+1)]
        for i in range(n+1):
            dist[i][i]=0
            
        for i in range(len(times)):
            u, v, w = times[i]
            dist[u][v] = w
        
        for m in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    dist[i][j]=min(dist[i][j],dist[i][m]+dist[m][j])
               
        cost=0
        for i in range(1,n+1):
            if dist[k][i]==float('inf'):
                return -1
            cost=max(cost,dist[k][i])
            
        return cost