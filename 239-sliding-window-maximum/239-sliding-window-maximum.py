class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n,i,j,res,temp=len(nums),0,0,[],[]
        while j<n:
            while temp!=[] and temp[-1]<nums[j]:
                temp.pop()
            temp.append(nums[j])
            if j-i+1==k:
                res.append(temp[0])
                if temp[0]==nums[i]:
                    temp.pop(0)
                i+=1
            j+=1
        return res