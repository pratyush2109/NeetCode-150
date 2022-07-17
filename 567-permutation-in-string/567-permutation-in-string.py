class Solution:
    def matches(self, d1, d2):
        for i in d1.keys():
            if i not in d2:
                return False
            if d1[i]!=d2[i]:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        
        if n1>n2:
            return False
        
        d1=dict()
        d2=dict()
        
        for i in range(n1):
            if s1[i] not in d1:
                d1[s1[i]]=1
            else:
                d1[s1[i]]+=1
            if s2[i] not in d2:
                d2[s2[i]]=1
            else:
                d2[s2[i]]+=1
                
        if d1==d2:
            return True
        
        for i in range(n1,n2):
            d2[s2[i-n1]]-=1
            if s2[i] not in d2:
                d2[s2[i]]=1
            else:
                d2[s2[i]]+=1
            if self.matches(d1,d2):
                return True
            
        return False