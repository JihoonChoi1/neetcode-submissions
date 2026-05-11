class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for i, j in counts.items():
            if (j >= len(nums) // 2):
                return int(i)
        return 0