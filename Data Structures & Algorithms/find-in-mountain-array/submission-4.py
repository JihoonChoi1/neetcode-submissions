class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l,r = 0, n - 1
        peakIndex = 0
        while l <= r:
            m = l + ((r-l) // 2)
            num = mountainArr.get(m)
            if num > mountainArr.get(m-1) and num > mountainArr.get(m+1):
                peakIndex = m
                break
            elif num < mountainArr.get(m-1):
                r = m - 1
            else:
                l = m + 1

        l,r = 0, peakIndex
        while l <= r:
            m = l + ((r-l) // 2)
            tmp = mountainArr.get(m)
            if tmp == target:
                return m
            elif tmp < target:
                l = m + 1
            else:
                r = m - 1
        
        l, r = peakIndex+1, n-1
        while l <= r:
            m = l + ((r-l) // 2)
            tmp =  mountainArr.get(m)
            if tmp == target:
                return m
            if tmp < target:
                r = m - 1
            else:
                l = m + 1
        return -1

        