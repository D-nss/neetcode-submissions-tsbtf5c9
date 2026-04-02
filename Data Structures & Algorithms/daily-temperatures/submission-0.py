class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Pode vir zerado?
        
        # Brute Force -> Para cada num vemos até achar uma temperatura maior que ele ou não achar
        # O(n * log n)

        # [30,38,30,36,35,40,28]
        # [38, 36]
        # r = 5
        # l = 1
        # [1,]

        stack = []
        saida = [0] * len(temperatures)

        print(saida)

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < temp:
                saida[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append([temp, i])
        
        return saida