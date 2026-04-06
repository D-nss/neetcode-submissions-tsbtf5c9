# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fim1 = list1
        fim2 = list2

        head = ListNode()
        head_cop = head

        while fim1 != None and fim2 != None:
            if fim1.val < fim2.val:
                head_cop.next= fim1
                head_cop = head_cop.next
                fim1 = fim1.next
            
            else:
                head_cop.next= fim2
                head_cop = head_cop.next
                fim2 = fim2.next

        if fim1 != None:
            head_cop.next= fim1

        if fim2 != None:
            head_cop.next= fim2

        return head.next
        