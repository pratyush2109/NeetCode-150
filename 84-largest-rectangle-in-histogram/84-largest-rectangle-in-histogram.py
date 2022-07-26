class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            startIdx = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                startIdx = idx
            stack.append((startIdx, heights[i])) # store (idx, height)
        
        for startIdx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - startIdx))
            
        return maxArea