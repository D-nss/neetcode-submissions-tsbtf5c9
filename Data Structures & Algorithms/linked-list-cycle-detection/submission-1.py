# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        l = head
        r = head.next

        while r != None:
            if r == l:
                return True
            
            l = l.next
            r = r.next
            if r != None:
                r = r.next

        return False


        