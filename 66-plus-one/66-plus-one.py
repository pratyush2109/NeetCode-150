class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st_digits=[str(i) for i in digits]
        s="".join(st_digits)
        
        ans=int(s)+1
        s_ans=str(ans)
        
        return list(s_ans)