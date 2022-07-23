class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        
        while low<high:
            mid=(low+high)//2
            hour_spent=0
            
            for i in piles:
                hour_spent+=math.ceil(i/mid)
                
            if hour_spent<=h:
                high=mid
            else:
                low=mid+1
                
        return high