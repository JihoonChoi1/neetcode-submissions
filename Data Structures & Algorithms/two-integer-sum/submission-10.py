class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        res = [0, 0]
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind in track:
                res[0] = track[toFind]
                res[1] = i
                break
            track[nums[i]] = i
        return res
        

