class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        if nums[0]==0:
            return False
        
        maxReach=nums[0]
        jumps=0
        for i in range(1,len(nums)):
            maxReach-=1
            if nums[i]>maxReach:
                maxReach=nums[i]
                jumps+=1
            if maxReach==0 and i!=len(nums)-1:
                return False
            if i==len(nums)-1:
                return True