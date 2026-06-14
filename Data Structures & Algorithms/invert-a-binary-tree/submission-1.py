# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        res = root
        while root or stack:
            while root:
                tmp = root.left
                root.left = root.right
                root.right = tmp
                if root.right:
                    stack.append(root.right)
                root = root.left
            if stack:
                root = stack.pop()
        return res

