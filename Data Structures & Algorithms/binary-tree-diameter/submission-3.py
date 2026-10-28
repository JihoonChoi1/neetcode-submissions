# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal maxi

            leftDiameter = dfs(node.left)
            rightDiameter = dfs(node.right)

            maxi = max(maxi, leftDiameter + rightDiameter)

            return 1 + max(leftDiameter, rightDiameter)

        dfs(root)
        return maxi

