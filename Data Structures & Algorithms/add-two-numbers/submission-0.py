# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        link = l1
        num1 = ""
        lista1 = []
        while link != None:
            lista1.append(link.val)
            link = link.next
        
        for i in range(len(lista1)):
            num1 += str(lista1[len(lista1) -1 -i])
        
        num1 = int(num1)
        

        link = l2
        num2 = ""
        lista2 = []
        while link != None:
            lista2.append(link.val)
            link = link.next

        for i in range(len(lista2)):
            num2 += str(lista2[len(lista2) -1 -i])

        num2 = int(num2)


        num = str(num1 + num2)

        saida = ListNode()

        node = saida

        for i in range(len(num)):
            nodeN = ListNode()
            node.next= nodeN
            node = node.next
            node.val= int(num[len(num)-1 - i])

        return saida.next




