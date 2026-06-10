# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        rightStart = slow.next
        slow.next = None
        leftHead =  head

        curr = rightStart
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        rightHead = prev

        newHead = leftHead
        
        while leftHead and rightHead:
            tmp = leftHead.next
            leftHead.next = rightHead
            leftHead = tmp
            tmp = rightHead.next
            rightHead.next = leftHead
            rightHead = tmp

        




        

