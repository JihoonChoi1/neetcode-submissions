class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k
        while l < r:
            mid = (l + r) // 2
            if abs(x - arr[mid]) <= abs(x - arr[mid+k]):
                r = mid
            else:
                l = mid + 1
        return arr[l:l+k]
