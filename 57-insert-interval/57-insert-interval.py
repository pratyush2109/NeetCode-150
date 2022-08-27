class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        res=[]
        tmp=intervals[0]
        n=len(intervals)
        
        for i in range(1,n):
            if tmp[1]>=intervals[i][0]:
                tmp[1]=max(tmp[1],intervals[i][1])
            else:
                res.append(tmp)
                tmp=intervals[i]
                
        res.append(tmp)
        return res