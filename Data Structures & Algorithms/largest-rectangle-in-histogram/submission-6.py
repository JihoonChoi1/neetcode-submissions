class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxHeight = 0
        for i in range(len(heights)):
            height = heights[i]
            leftMax = i 
            rightMax = i
            while leftMax > 0 and heights[leftMax - 1] >= height:
                leftMax -= 1
            while rightMax < n-1 and height <= heights[rightMax+1]:
                rightMax += 1
            maxHeight = max(maxHeight, (rightMax-leftMax+1)*height)
        return maxHeight
            