# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        
        prev_temp = None
        while second:
            next_node = second.next
            second.next = prev_temp
            prev_temp = second
            second = next_node
        
        second = prev_temp
        first = head

        dummy = ListNode()
        temp = dummy
        while first and second:
            temp.next = first
            first = first.next
            temp.next.next = second
            second = second.next
            temp = temp.next.next
        temp.next = first
            



        
