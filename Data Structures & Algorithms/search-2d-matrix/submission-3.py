class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        rowSize = len(matrix)
        colSize = len(matrix[0])

        r = (rowSize * colSize) - 1
        while l <= r:
            mid = l + (r-l) // 2
            rowIdx = mid // colSize
            colIdx = mid % colSize
            currNum = matrix[rowIdx][colIdx]
            if  currNum == target:
                return True
            elif currNum < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
