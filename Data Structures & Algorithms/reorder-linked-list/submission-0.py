# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or  not head.next:
            return 

        s = head
        f = head.next

        while f.next != None:
            s = s.next
            copy = f.next
            if copy.next == None:
                f = copy
                break
            f = copy.next
        
        copy = s.next
        s.next = None
        s = copy
        prox = s.next
        s.next = None

        while prox != None:
            copy = prox.next
            prox.next = s
            s = prox
            prox = copy
            
        i = head
        verifica = 0
        while i != None and f != None :
            if verifica == 0:
                copy = i.next
                i.next = f
                i = copy
                verifica = 1
                print(f.val)
            else:
                copy = f.next
                f.next = i
                f = copy
                verifica = 0
        

