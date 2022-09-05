class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])
        n=rows
        edges=[]
        count=n
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c]==1 and r!=c:
                    edges.append([r+1,c+1])
        
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)
        
        def find(n):
            p=n
            while p!=parent[p]:
                parent[p]=parent[parent[p]]
                p=parent[p]
            return p
        
        def union(n1,n2):
            p1=find(n1)
            p2=find(n2)
            
            if p1==p2:
                return 0
            
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return 1
        
        for n1,n2 in edges:
            count-=union(n1,n2)
                
        return count
            