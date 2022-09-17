class Solution:
    def sumHappy(self, s):
        l=list(str(s))
        ans=0
        for i in l:
            ans+=int(i)**2
            
        return ans
    
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        visit=[n]
        while True:
            new=self.sumHappy(visit[-1])
            if new in visit:
                return False
            if new==1:
                return True
            visit.append(new)