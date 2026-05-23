class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > maxA:
                maxA = area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxA
