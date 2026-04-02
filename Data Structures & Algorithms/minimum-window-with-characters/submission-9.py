class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # lowercase sensitive?
        # pode vir vazio?
        # podem ser numeros?

        # Brute force -> percorrer cada substring possível de s e ver se ela possui t, selecionar a menor O(n^2)

        # 2 ponteiros -> l,r -> p, buscar um elemento de t em s, ao achar r +=1 (se não achar r += 1, l = r)
        # dicionario com a quantidade de cada letra em t
        # achando um, levamos o l para o indice do segundo encontrado
        # stack  -> fila, count = 0, fila[count:]
        # min(res, r - l + 1)
        # preciso guardar os obtidos

        dic_t ={}
        dic_repitidas = {}
        tam_real = 0
        index = []

        janela = []
        saida = []

        for letra in t:
            if letra in dic_t:
                dic_t[letra] += 1
            else:
                dic_t[letra] = 1
                dic_repitidas[letra] = 0

        r, l = 0, 0

        while r < len(s):
            if s[r] in dic_t:
                dic_repitidas[s[r]] += 1
                if dic_repitidas[s[r]] <= dic_t[s[r]]:
                    tam_real += 1
                    index.append(r)
                janela.append(s[r])
                if tam_real == len(t):
                    return s[r]
                r += 1
                break
            else:
                r += 1
                l = r

        count = 0
        while r < len(s):
            if s[r] in dic_t:
                dic_repitidas[s[r]] += 1
                if dic_repitidas[s[r]] <= dic_t[s[r]]:
                    tam_real += 1
                index.append(r)
                janela.append(s[r])
                print(janela)
                print(dic_repitidas)
                print(tam_real)
                if tam_real == len(t):
                    while tam_real == len(t):
                        saida.append(janela)
                        janela = janela[index[count + 1] - index[count]:]
                        l = count

                        if dic_repitidas[s[index[count]]] < dic_t[s[index[count]]] +1:
                            tam_real -= 1
                        print(janela)
                        print(dic_repitidas)
                        print(tam_real)
                        print(index)
                        dic_repitidas[s[index[count]]] -=1
                        count +=1
            else:
                janela.append(s[r])

            r += 1
    
        mini = 100000
        min_janela = []
        for i in saida:
            if mini > len(i):
                mini = len(i)
                min_janela = i
        
        return ''.join(min_janela)


        

        
        


