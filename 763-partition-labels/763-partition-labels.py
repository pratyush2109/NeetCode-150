class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s)==1:
            return [1]
        
        lastIndex={}
        for i in range(len(s)):
            lastIndex[s[i]]=i
            
        size=0
        end=0
        res=[]
        for i in range(len(s)):
            size+=1
            tmp_last=lastIndex[s[i]]
            if tmp_last>end:
                end=tmp_last
            if size+sum(res)>end:
                res.append(size)
                size=0
        
        return res