class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        res=[]
        tmp=intervals[0]
        
        for i in range(1,n):
            if tmp[1]>=intervals[i][0]:
                tmp[1]=max(tmp[1],intervals[i][1])
            else:
                res.append(tmp)
                tmp=intervals[i]
                
        res.append(tmp)
        return res