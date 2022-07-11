class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        
        for i in range(n-2):
            j=i+1
            k=n-1
            target=0
            target-=nums[i]
            while j<k:
                if nums[j]+nums[k]>target:
                    k-=1
                elif nums[j]+nums[k]<target:
                    j+=1
                else:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    
        return res