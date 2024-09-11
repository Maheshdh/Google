# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        cur = dummy_node
        first, second = list1,list2
        while first and second:
            if first.val <= second.val:
                cur.next = first
                first = first.next
                cur = cur.next
            else:
                cur.next = second
                second = second.next
                cur = cur.next
        if first:
            cur.next = first
        if second:
            cur.next = second
        return dummy_node.next
    

   
