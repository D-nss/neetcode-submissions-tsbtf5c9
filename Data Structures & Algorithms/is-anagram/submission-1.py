class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lista_s = []
        lista_t = []

        for letra in s:
            lista_s.append(letra)

        for letra in t:
            lista_t.append(letra)

        for letra in lista_s:
            if letra in lista_t:
                index = lista_t.index(letra)
                lista_t.pop(index)
            else:
                return False
        if len(lista_t) != 0:
            return False
        return True