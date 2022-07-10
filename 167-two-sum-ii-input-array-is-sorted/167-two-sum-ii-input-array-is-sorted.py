class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        if n==2:
            return [1,2]
        
        low=0
        high=n-1
        while low<high:
            if numbers[low]+numbers[high]==target:
                return [low+1,high+1]
            elif numbers[low]+numbers[high]>target:
                high-=1
            else:
                low+=1