class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = 0
        count1 = 0
        candidate2 = 0
        count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            else:
                if count1 == 0:
                    candidate1 = num
                    count1 += 1
                elif count2 == 0:
                    candidate2 = num
                    count2 += 1
                else:
                    count1 -= 1
                    count2 -= 1
        arr = [candidate1, candidate2]
        res = []
        for num in arr:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res


                    