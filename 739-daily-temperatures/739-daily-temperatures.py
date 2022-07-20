class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        n = len(temperatures)
        
        for i in range(n):
            while s and s[-1][1]<temperatures[i]:
                d = s.pop()
                temperatures[d[0]]=i-d[0]
            s.append([i,temperatures[i]])
        
        while s:
            d=s.pop()
            temperatures[d[0]]=0
            
        return temperatures