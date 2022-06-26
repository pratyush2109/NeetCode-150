class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=dict()
        flag=0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
                flag=1
                
        if flag==1:
            return True
        else:
            return False