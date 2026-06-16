# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "$#"
            
        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serializedRoot = self.serialize(root)
        serializedSubRoot = self.serialize(subRoot)

        return True if serializedSubRoot in serializedRoot else False