class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = [0,0]
        r = [m-1, n-1]
        while l[0] <= r[0] and l[1] <= r[1]:
            mid = [l[0] + ((r[0] - l[0]) // 2), l[1] + ((r[1] - l[1]) // 2)]
            num = matrix[mid[0]][mid[1]]
            if num == target:
                return True
            elif num < target:
                if l[1] < n - 1:
                    l[1] += 1
                else:
                    l[0] += 1
                    l[1] = 0
            else:
                if r[1] > 0:
                    r[1] -= 1
                else:
                    r[0] -= 1
                    r[1] = n - 1
        return False