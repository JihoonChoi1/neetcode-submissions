# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev_tail = dummy
        for _ in range(left-1):
            prev_tail = prev_tail.next
        
        cur = prev_tail.next
        prev = None
        while left <= right:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            left += 1
        
        prev_tail.next.next = cur
        prev_tail.next = prev

        return dummy.next





        