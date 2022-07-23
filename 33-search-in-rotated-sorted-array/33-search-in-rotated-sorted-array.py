class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        
        while left<=right:
            middle=left + (right-left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>=nums[left]:
                if nums[left]<=target<nums[middle]:
                    right=middle-1
                else:
                    left=middle+1
            else:
                if nums[middle]<target<=nums[right]:
                    left=middle+1
                else:
                    right=middle-1
                    
        return -1