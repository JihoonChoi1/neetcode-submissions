class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        arr = [0] * (len(left) + len(right))
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
