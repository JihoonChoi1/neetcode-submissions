class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = count = 0
        
        sign = -1
        n = len(arr)

        for i in range(n-1):
            if arr[i] < arr[i+1]:
                count = count + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] > arr[i+1]:
                count = count + 1 if sign == 1 else 1
                sign = 0
            else:
                count = 0
                sign = -1

            res = max(res, count)

        return res + 1
            

