class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pode vir zerado?
        # um carro pode ter velocidade zero?
        # um carro pode ja estar no target ou estar na frente?

        # Brute force -> aumento uma hora e calculo a posição para cada carro, vejo se alguem alcançou alguém, mudo a velocidade do carro
        # que alcançou para a do carro alcançado, por cada momento calculado, vejo se chegou alguém, se chegou somo +1

        # O(n*k)

        # [4, 1, 0, 7]          [[0,10], [1, 2], [4, 3], [7, 3]]
        # [2, 2, 1, 1]

        # [3, 4,5, 10, 3]

        # ideia -> calcula o tempo, da um sort pela pos ini, faz um stack que ve se o proximo é menor

        tempo = []

        if len(position) == 1:
            return 1

        if len(position) == 0:
            return 0

        for i, pos in enumerate(position):
            t = (target - pos)/speed[i]
            tempo.append([pos, t])
        
        lista = sorted(tempo)

        saida = []

        print(lista)
    
        for i in range(len(lista)):
            while len(saida) > 0 and lista[i][1] >= saida[-1][1]:
                saida.pop()
            saida.append(lista[i])
                
            

        return len(saida)
        