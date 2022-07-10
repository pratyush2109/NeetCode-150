class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 or n==0:
            return n
        
        nums.sort()
        max_ans=1
        ans_till_here=1
        
        for i in range(1,n):
            if nums[i]-nums[i-1]==1:
                ans_till_here+=1
            elif nums[i]-nums[i-1]>1:
                ans_till_here=1
                
            if ans_till_here>max_ans:
                max_ans=ans_till_here
                
        return max_ans