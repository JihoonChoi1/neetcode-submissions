class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m
                
        peakIndex = l
        
        l, r = 0, peakIndex
        while l <= r:
            m = l + (r - l) // 2
            tmp = mountainArr.get(m)
            if tmp == target:
                return m
            elif tmp < target:
                l = m + 1
            else:
                r = m - 1
                
        l, r = peakIndex + 1, n - 1
        while l <= r:
            m = l + (r - l) // 2
            tmp = mountainArr.get(m)
            if tmp == target:
                return m
            elif tmp < target:
                r = m - 1
            else:
                l = m + 1
                
        return -1