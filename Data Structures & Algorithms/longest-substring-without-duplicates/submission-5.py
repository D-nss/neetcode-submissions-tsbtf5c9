class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #lowercase?
        #só letras?
        #pode vir vazia?
        #bruteForce -> Percorer por cada caracter armazenando em uma lista os usados, acada avanço verificar se o caracter novo está na lista
        #O(n^2)

        #solução: dic com a posição da fila, fila, exclui valores anteriores
        #abcabcbb
        dic = {}
        fila = []
        count = 0
        res = 0

        for i in range(len(s)):
            if s[i] in dic:
                count = max(dic[s[i]] + 1, count)

            dic[s[i]] = i
            fila.append(s[i])
            res = max(res, len(fila[count:]))
    
        return res


