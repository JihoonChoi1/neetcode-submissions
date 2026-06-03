class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []
        res = 0
        for p, s in pairs:
            leftTime = (target - p) / s
            if not stack or leftTime > stack[-1]:
                res += 1
                stack.append(leftTime)        
        return res
        

