class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lista_final = []
        while len(strs) > 0:
            palavra = strs[0]
            index = strs.index(palavra)
            strs.pop(index)

            grupo = [palavra]

            lista_palavra = [i for i in palavra]

            for palavra_escolhida in strs[:]:
                # ver se o len é =
                # ver se cada letra esta na palvra - remover letra por letra

                lista_palavra_escolhida = [i for i in palavra_escolhida]

                if len(lista_palavra_escolhida) == len(lista_palavra):
                    for letra in lista_palavra:
                        if letra in lista_palavra_escolhida:
                            index = lista_palavra_escolhida.index(letra)
                            lista_palavra_escolhida.pop(index)

                    if len(lista_palavra_escolhida) == 0:
                        grupo.append(palavra_escolhida)
                        index = strs.index(palavra_escolhida)
                        strs.pop(index)

            lista_final.append(grupo)

        return lista_final

