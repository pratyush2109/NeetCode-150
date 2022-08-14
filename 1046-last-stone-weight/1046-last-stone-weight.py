import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        
        arr=[-1*i for i in stones]
        heapq.heapify(arr)
        
        while len(arr)!=0 and len(arr)!=1:
            y=heapq.heappop(arr)
            x=heapq.heappop(arr)
            if x!=y:
                heapq.heappush(arr,y-x)
                
        if len(arr)==0:
            return 0
        else:
            return -1*arr[0]