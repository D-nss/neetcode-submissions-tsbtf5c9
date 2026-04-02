class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # index_menor < index_maior
        # se negativo devolve 0
        # brute force -> verificar cada combinação 0(n * log(n))
        # O(n) -> 2 ponteiro
        # l > r -> l + 1
        # [2,1,2,1,0,1,2]
        # [10,1,5,6,7,1]

        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                res = max(res, prices[r] - prices[l] )
                r +=1

        return res


        7 - 4
        7 - 6


        

