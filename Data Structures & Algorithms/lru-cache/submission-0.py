class Node:
    def __init__(self, key=0, val=0):
        self.key = key  
        self.val = val
        self.ant = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.maxi = capacity
        self.dic = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.ant = self.head

    def _remover_da_lista(self, node):
        ant = node.ant
        prox = node.next
        ant.next = prox
        prox.ant = ant

    def _adicionar_ao_fim(self, node):
        ultimo_real = self.tail.ant
        ultimo_real.next = node
        node.ant = ultimo_real
        node.next = self.tail
        self.tail.ant = node

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remover_da_lista(node) 
            self._adicionar_ao_fim(node) 
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remover_da_lista(self.dic[key])
        
        novo_no = Node(key, value)
        self.dic[key] = novo_no
        self._adicionar_ao_fim(novo_no)
        
        if len(self.dic) > self.maxi:
            lru_node = self.head.next
            self._remover_da_lista(lru_node)
            del self.dic[lru_node.key] 