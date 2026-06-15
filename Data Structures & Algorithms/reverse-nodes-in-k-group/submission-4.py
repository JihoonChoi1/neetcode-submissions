# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = k
        dummy = ListNode()
        dummy.next = head
        prevTail = dummy
        while head:
            prevHead = head
            while i > 0 and head:
                head = head.next
                i -= 1
            if i == 0:
                cur = prevHead
                prev = None
                while cur != head:
                    tmp1 = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp1
                prevTail.next = prev
                prevTail = prevHead
                prevHead.next = cur
                i = k 
        return dummy.next
                

