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
        aponta = {}
        ponteiro = {}
        if not head:
            return None
        
        count = 0
        contador = 101
        
        link = head
        while link != None:
            if link.val not in ponteiro:
                pont = Node(link.val, None, None)
                link.val = contador
                ponteiro[contador] = pont
                contador +=1
            
            point = ponteiro[link.val]

            if count == 0:
                saida = point
                count = 1

            if link.next != None:
                if link.next.val not in ponteiro:
                    pont = Node(link.next.val, None, None)
                    link.next.val = contador
                    ponteiro[contador] = pont
                    contador +=1
                point.next = ponteiro[link.next.val]

            if link.random != None:
                if link.random.val not in ponteiro:
                    pont = Node(link.random.val, None, None)
                    link.random.val = contador
                    ponteiro[contador] = pont
                    contador +=1
                point.random = ponteiro[link.random.val]
            
            link = link.next
            
        return saida
        