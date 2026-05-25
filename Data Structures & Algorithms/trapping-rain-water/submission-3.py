class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL < maxR:
                res += maxL - height[l]
                l += 1
            else:
                res += maxR - height[r]
                r -= 1
        return res
