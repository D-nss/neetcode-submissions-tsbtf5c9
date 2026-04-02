class Solution:
    def busca (self, ini, fim, lista, saida, h):
        if ini <= fim:
            media = ini + (fim - ini)//2
            count = 0
            for i in lista:
                count += (i + media - 1) // media
            if count > h:
                return min(saida, self.busca(media +1, fim, lista, saida, h))
            else:
                return min(media, self.busca(ini, media -1, lista, media, h))
                
        else:
            return saida  

        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        mini = 1
        maxi = max(piles)

        res = self.busca(mini, maxi, piles, maxi, h)

        return res



        
        