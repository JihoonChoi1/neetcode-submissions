# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        def merge(list1, list2):
            dummy = ListNode()
            tmp = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    tmp.next = list1
                    list1 = list1.next
                else:
                    tmp.next = list2
                    list2 = list2.next
                tmp = tmp.next
            if list1:
                tmp.next = list1
            else:
                tmp.next = list2
            return dummy.next
 
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(merge(l1,l2))
            lists = mergedLists
        
        return lists[0]


                




        