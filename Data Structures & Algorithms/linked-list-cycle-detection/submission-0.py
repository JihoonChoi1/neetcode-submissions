# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slowNode = head
        fastNode = head.next
        while fastNode != None:
            if slowNode == fastNode:
                return True
            if fastNode.next != None:
                fastNode = fastNode.next.next
            else:
                return False
            slowNode = slowNode.next
        return False
