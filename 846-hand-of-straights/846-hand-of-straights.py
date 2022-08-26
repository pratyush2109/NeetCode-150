import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        
        count={}
        for i in hand:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
                
        minHeap=list(count.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            first=minHeap[0]
            
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
                    
        return True