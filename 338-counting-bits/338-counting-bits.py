class Solution:
    def countOne(self, m):
        res=0
        while m:
            m&=(m-1)
            res+=1
        return res

    def countBits(self, n: int) -> List[int]:
        ans=[]
        i=0
        while i<=n:
            ans.append(self.countOne(i))
            i+=1
            
        return ans