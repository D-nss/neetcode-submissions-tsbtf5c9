class Solution:
    def busca(self, ini, fim, lista, target): # 
        meio = ini + (fim -ini)//2

        if ini <= fim:
            if lista[meio] == target:
                return True

            elif lista[meio] < target:
                return self.busca(meio +1, fim, lista, target)

            elif lista[meio] > target:
                return self.busca(ini, meio -1, lista, target)
        else:
            return False

    
    def buscaCol(self, ini, fim, lista, target):
        meio = ini + (fim -ini)//2
        if ini <= fim:
            if lista[meio][0] <= target:
                if lista[meio][-1] >= target:
                    return meio
                else:
                    return self.buscaCol(meio +1, fim, lista, target)
            else:
                return self.buscaCol(ini, meio -1, lista, target)
        
        else:
            return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = self.buscaCol(0, len(matrix) -1, matrix, target)

        if col == -1:
            return False

        return self.busca(0, len(matrix[0]) -1, matrix[col], target)

        