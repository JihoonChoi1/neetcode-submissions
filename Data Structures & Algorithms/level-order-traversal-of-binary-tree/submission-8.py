# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        q = deque()
        res = []
        q.append(root)

        while q:
            tmp = []
            size = len(q)
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    tmp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if tmp:
                res.append(tmp)

        return res



        