"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        dummy = Node(0)
        copy = dummy
        temp = head

        while temp:
            new_node = Node(temp.val)
            copy.next = new_node
            old_to_new[temp] = new_node
            copy = copy.next
            temp = temp.next
        
        copy = dummy.next

        while head:
            if head.random:
                copy.random = old_to_new[head.random]
            head = head.next
            copy = copy.next

        return dummy.next


        
        
        