# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = k
        dummy = ListNode()
        dummy.next = head
        prevTail = dummy
        while head:
            prevHead = head
            while count > 0 and head:
                head = head.next
                count -= 1
            if count == 0:
                cur = prevHead
                prev = None
                while cur != head:
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp
                prevTail.next = prev
                prevTail = prevHead
                prevHead.next = cur
                count = k 
        return dummy.next
                

