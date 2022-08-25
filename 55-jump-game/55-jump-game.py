class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        if nums[0]==0:
            return False
        if n==1:
            return True
        
        maxReach=nums[0]
        jumps=1
        step=nums[0]
        
        for i in range(1,n):
            if i==n-1:
                return True
            else:
                maxReach=max(maxReach,i+nums[i])
                step-=1
                if step==0:
                    if maxReach<=i:
                        return False
                    else:
                        jumps+=1
                        step=maxReach-i