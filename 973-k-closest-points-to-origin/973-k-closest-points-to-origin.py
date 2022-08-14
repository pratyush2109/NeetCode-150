import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap=[]
        for point in points:
            dist=math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(min_heap, (dist,point))
            
        return [x[1] for x in heapq.nsmallest(k, min_heap)]