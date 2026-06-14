# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        prev = None
        res = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]
            if root.right and root.right != prev:
                root = root.right
            else:
                res.append(root.val)
                stack.pop()
                prev = root
                root = None
        return res
            

