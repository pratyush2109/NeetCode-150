class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        l=0
        res=0
        max_freq=0
        
        for r in range(len(s)):
            count[s[r]]+=1
            if count[s[r]]>max_freq:
                max_freq=count[s[r]]
            if (r-l+1)-max_freq>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        
        return res