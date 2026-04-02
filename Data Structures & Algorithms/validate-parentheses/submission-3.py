class Solution:
    def tipo_valido(self, s1, s2) -> bool:
        gp = [['[', ']'], ['(', ')'], ['{', '}']]

        for grupo in gp:
            if s1 in grupo and s2 in grupo:
                return True
        
        return False
    
    def isFechamento(self, s) -> bool:
        gp = [ ']', ')', '}']

        if s in gp:
            return True
        
        else:
            return False




    def isValid(self, s: str) -> bool:
    # Pode vir uma string vazia?
    # poderia adicionar uma checagem par ver se é um dos 3 tipos de abertura

    # Len(s) % 2 = 0?

    # Brute force -> pra cada index -> tenho que ver se o primeiro feichamento que aparece tem como ultima abertura do mesmo tipo
    # O(n* log n)

    # Poderia ter duas lista, onde uma seria para abertura e outra para fechamento, 
    # sempre que colocar u fechamento ver o ultimo valor da de abertura e comparar, se sim pop no final da lista

        abertura = []
        fechamento = []

        if len(s) % 2 != 0:
            return False

        for chave in s:
            if self.isFechamento(chave):
                fechamento.append(chave)
                if len(abertura) < 1:
                    return False
                if not self.tipo_valido(chave, abertura[-1]):
                    return False
                abertura.pop()
                fechamento.pop()

            else:
                abertura.append(chave)
        
        if len(abertura) == 0 and len(fechamento) == 0:
            return True
        
        else:
            return False



        