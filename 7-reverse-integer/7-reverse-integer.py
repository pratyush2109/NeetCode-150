class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            ans=int(str(x)[::-1])
        elif x==0:
            return 0
        else:
            sx=str(x)[1:]
            ans=int(sx[::-1])*-1
            
        if ans>2**31-1 or ans<-2**31:
            return 0
        return ans