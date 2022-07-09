class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(set(nums))==k:
            list(set(nums))
            
        d=dict()
        n=len(nums)
        
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        d=sorted(d.items(),key=lambda x:x[1],reverse=True)
        ind=0
        res=[]
        while ind<k:
            res.append(d[ind][0])
            ind+=1
            
        return res