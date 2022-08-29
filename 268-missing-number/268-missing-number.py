class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        req = (n*(n+1))//2
        total = sum(nums)
        
        return req-total