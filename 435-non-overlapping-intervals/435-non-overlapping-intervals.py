class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        tmp=intervals[0]
        n=len(intervals)
        
        for i in range(1,n):
            if tmp[1]>intervals[i][0]:
                count+=1
                tmp[1]=min(tmp[1],intervals[i][1])
            else:
                tmp=intervals[i]
                
        return count