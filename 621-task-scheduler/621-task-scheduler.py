import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        
        count=Counter(tasks)
        max_heap=[-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        queue=deque() # pairs of [-cnt,Time it will available to add to heap back]
        time=0
        
        while max_heap or queue:
            time+=1
            if max_heap:
                count=1+heapq.heappop(max_heap)
                if count!=0:
                    queue.append([count,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(max_heap, queue.popleft()[0])
                
        return time