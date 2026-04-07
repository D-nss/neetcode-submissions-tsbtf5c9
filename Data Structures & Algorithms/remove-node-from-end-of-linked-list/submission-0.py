# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #contamos o tamanho
        #chegamos no que queremos remover

        count = 0
        link = head

        while link != None:
            link = link.next
            count +=1

        count = count - n

        link = head
        print(count)
        if count > 0:
            for i in range(count -1):
                link = link.next

            link.next = link.next.next
            
            return head

        else:
            return link.next


