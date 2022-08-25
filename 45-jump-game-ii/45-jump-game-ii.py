class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        
        maxReach=nums[0]
        jumps=1
        step=nums[0]
        
        for i in range(1,n):
            if i==n-1:
                return jumps
            else:
                maxReach=max(maxReach,i+nums[i])
                step-=1
                if step==0:
                    if maxReach<=i:
                        return -1
                    else:
                        jumps+=1
                        step=maxReach-i