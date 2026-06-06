class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0
        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                tmp = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                height = heights[tmp]
                maxArea = max(maxArea, width*height)
            stack.append(i)
        return maxArea