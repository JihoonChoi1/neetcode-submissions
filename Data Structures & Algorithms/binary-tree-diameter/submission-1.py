# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxi = 0

        def getDiameter(root):
            nonlocal maxi
            if not root:
                return 0

            rightDiameter = getDiameter(root.right)
            leftDiameter = getDiameter(root.left)
            maxi = max(maxi, rightDiameter + leftDiameter)

            return 1 + max(rightDiameter, leftDiameter)

        getDiameter(root)
        return maxi


            