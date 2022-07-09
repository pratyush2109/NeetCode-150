class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for i in strs:
            tmp=sorted(i)
            tmp="".join(tmp)
            if tmp not in d:
                d[tmp]=[i]
            else:
                d[tmp].append(i)
            
        res=[]
        for i in d.keys():
            res.append(d[i])
            
        return res