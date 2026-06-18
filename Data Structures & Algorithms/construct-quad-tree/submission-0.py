"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(n, row,col):
            if n == 1:
                return Node(grid[row][col] == 1, True)
            n = n // 2
            topLeft = dfs(n, row, col)
            topRight = dfs(n, row, col+n)
            bottomLeft = dfs(n, row+n, col)
            bottomRight = dfs(n, row+n, col+n)
            if (topLeft.isLeaf and topRight.isLeaf and 
                bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val == 1, True)
            else:
                return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(len(grid), 0, 0)
            

